from _collections_abc import Generator
import types
import asyncio


async def compute(a: int, b: int) -> int:
    print('Compute...')
    await asyncio.sleep(1)
    return a + b


print(next(compute(3, 5).__await__()))