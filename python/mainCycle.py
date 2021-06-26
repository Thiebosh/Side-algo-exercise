from domain.Point import Point
from domain.Path import Path
from parsing.readFromResources import cycle
from cycle import shortCycle
import random
from functools import lru_cache
import time


def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap


@lru_cache()
def pointsInGrid(width: int, height: int) -> "list[Point]":
    return [Point(x, y) for x in range(width) for y in range(height)]


def printResult(path: Path) -> None:
    print(f"{path.length()}\n{','.join(map(lambda x: str(x), path.points[::-1]))}\n\n")
    # display gaph too, because, ya know... => visual


# @timing
def mainCycle() -> None:
    # seed = args, from str to float
    # random.seed()

    shortCycle(pointsInGrid(10, 8))

    print("80 points in a 8x10 grid")
    printResult(shortCycle(shuffle(pointsInGrid(10, 8))))

    # take 40ms to generate only
    # print("200 random points")
    # printResult(shortCycle(shuffle([pointsInGrid(random.randint(0, 700), random.randint(0, 700)) for _ in range(200)])))

    print("File 14 nodes")
    printResult(shortCycle(cycle("14_nodes.txt")))

    print("File 52 nodes")
    printResult(shortCycle(cycle("52_nodes.txt")))

    print("File 202 nodes")
    printResult(shortCycle(cycle("202_nodes.txt")))

    # more than 1000 depth recursion allowed by python
    # print("File 1002 nodes")
    # printResult(shortCycle(cycle("1002_nodes.txt")))

    # print("File 5915 nodes")
    # printResult(shortCycle(cycle("5915_nodes.txt")))


def shuffle(grid: list) -> list:
    random.shuffle(grid)
    return grid


if __name__ == "__main__":
    mainCycle()
