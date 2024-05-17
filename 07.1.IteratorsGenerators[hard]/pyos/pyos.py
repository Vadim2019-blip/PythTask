from queue import Queue
from abc import ABC, abstractmethod
from typing import Generator, Optional, Any, Dict, List


class SystemCall(ABC):
    """SystemCall yielded by Task to handle with Scheduler"""

    @abstractmethod
    def handle(self, scheduler: 'Scheduler', task: 'Task') -> bool:
        """
        :param scheduler: link to scheduler to manipulate with active tasks
        :param task: task which requested the system call
        :return: an indication that the task must be scheduled again
        """


Coroutine = Generator[Optional[SystemCall], Any, None]


class Task:
    def __init__(self, task_id: int, target: Coroutine) -> None:
        """
        :param task_id: id of the task
        :param target: coroutine to run. Coroutine can produce system calls.
        System calls are being executed by scheduler and the result sends back to coroutine.
        """
        self.task_id = task_id
        self.target = target
        self.syscall_result = None

    def set_syscall_result(self, result: Any) -> None:
        """
        Saves result of the last system call
        """
        self.syscall_result = result

    def step(self) -> Optional[SystemCall]:
        """
        Performs one step of coroutine, i.e. sends result of last system call
        to coroutine (generator), gets yielded value and returns it.
        """
        try:
            if self.syscall_result is not None:
                result = self.target.send(self.syscall_result)
                self.syscall_result = None
            else:
                result = next(self.target)
            return result
        except StopIteration:
            return None


class Scheduler:
    """Scheduler to manipulate with tasks"""

    def __init__(self) -> None:
        self.task_id = 0
        self.task_queue: Queue[Task] = Queue()
        self.task_map: dict[int, Task] = {}  # task_id -> task
        self.wait_map: dict[int, list[Task]] = {}  # task_id -> list of waiting tasks

    def _schedule_task(self, task: Task) -> None:
        """Add task into task queue
        :param task: task to schedule for execution
        """
        self.task_queue.put(task)

    def new(self, target: Coroutine) -> int:
        """Create and schedule new task
        :param target: coroutine to wrap in task
        :return: id of newly created task
        """
        self.task_id += 1
        task = Task(self.task_id, target)
        self.task_map[self.task_id] = task
        self._schedule_task(task)
        return self.task_id

    def exit_task(self, task_id: int) -> bool:
        """PRIVATE API: can be used only from scheduler itself or system calls
        Hint: do not forget to reschedule waiting tasks
        :param task_id: task to remove from scheduler
        :return: true if task id is valid
        """
        if task_id not in self.task_map:
            return False
        task = self.task_map.pop(task_id)
        waiting_tasks = self.wait_map.pop(task_id, [])
        for waiting_task in waiting_tasks:
            self._schedule_task(waiting_task)
        return True

    def wait_task(self, task_id: int, wait_id: int) -> bool:
        """PRIVATE API: can be used only from scheduler itself or system calls
        :param task_id: task to hold on until another task is finished
        :param wait_id: id of the other task to wait for
        :return: true if task and wait ids are valid task ids
        """
        if task_id not in self.task_map or wait_id not in self.task_map:
            return False
        self.wait_map.setdefault(wait_id, []).append(self.task_map[task_id])
        return True

    def run(self, ticks: Optional[int] = None) -> None:
        """Executes tasks consequently, gets yielded system calls,
        handles them and reschedules task if needed
        :param ticks: number of iterations (task steps), infinite if not passed
        """
        tick = 0
        while ticks is None or tick < ticks:
            tick += 1
            if self.task_queue.empty():
                continue
            task = self.task_queue.get()
            result = task.step()
            if result is not None:
                reschedule = result.handle(self, task)
                if reschedule:
                    self._schedule_task(task)
            else:
                self.exit_task(task.task_id)

    def empty(self) -> bool:
        """Checks if there are some scheduled tasks"""
        return not bool(self.task_map)


class GetTid(SystemCall):
    """System call to get current task id"""

    def handle(self, scheduler: Scheduler, task: Task) -> bool:
        task.set_syscall_result(task.task_id)
        return True


class NewTask(SystemCall):
    """System call to create new task from target coroutine"""

    def __init__(self, target: Coroutine) -> None:
        self.target = target

    def handle(self, scheduler: Scheduler, task: Task) -> bool:
        task.set_syscall_result(scheduler.new(self.target))
        return True


class KillTask(SystemCall):
    """System call to kill task with particular task id"""

    def __init__(self, task_id: int) -> None:
        self.task_id = task_id

    def handle(self, scheduler: Scheduler, task: Task) -> bool:
        task.set_syscall_result(scheduler.exit_task(self.task_id))
        return False


class WaitTask(SystemCall):
    """System call to wait task with particular task id"""

    def __init__(self, task_id: int) -> None:
        self.task_id = task_id

    def handle(self, scheduler: Scheduler, task: Task) -> bool:
        # Note: One shouldn't reschedule task which is waiting for another one.
        # But one must reschedule task if task id to wait for is invalid.
        task.set_syscall_result(scheduler.wait_task(task.task_id, self.task_id))
        return not task.syscall_result