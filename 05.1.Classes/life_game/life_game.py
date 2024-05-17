import copy

class LifeGame(object):
    """
    Class for Game life
    """
    def __init__(self, field):
        self.field = field
    def _get_neighbours(self,copy1, i: int, j: int):
        neighbours = []
        for t1 in {-1, 0, 1}:
            for t2 in {-1, 0, 1}:
                if (
                        0 <= i + t1 < len(copy1)
                        and 0 <= j + t2 < len(copy1[i])
                        and not (t1 == 0 and t2 == 0)):
                    neighbours.append(copy1[i + t1][j + t2])
        return neighbours
    def get_next_generation(self):
        copy1 = copy.deepcopy(self.field)
        copy2 = copy.deepcopy(self.field)
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                neighbours = self._get_neighbours(copy1, i, j)
                print(i, j, neighbours, copy2)
                if copy2[i][j] == 1:
                    continue
                elif copy2[i][j] == 2:
                    if neighbours.count(2) >= 4 or neighbours.count(2) <= 1:
                        self.field[i][j] = 0
                elif copy2[i][j] == 3:
                    if neighbours.count(3) >= 4 or neighbours.count(3) <= 1:
                        self.field[i][j] = 0
                elif copy2[i][j] == 0:
                    if neighbours.count(2) == 3:
                        self.field[i][j] = 2
                    elif neighbours.count(3) == 3:
                        self.field[i][j] = 3
        return self.field

a = LifeGame([
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])
for i in range(10):
    a.get_next_generation()
print(a.get_next_generation())
print('_______________________ RIGHT')
print([
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 2, 0],
            [0, 2, 0, 0, 0, 0, 0, 2, 0],
            [0, 2, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])