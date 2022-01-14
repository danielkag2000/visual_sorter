import random
from algs import SORTERS
from algs import AlgAnimation

CHOOSE_SORTER = """
Choose sorter:
1. bubble sort
2. insertion sort
3. quick sort
4. merge sort
5. heap sort
"""

CHOICE = {
    1: SORTERS.BUBBLE,
    2: SORTERS.INSERTION,
    3: SORTERS.QUICK,
    4: SORTERS.MERGE,
    5: SORTERS.HEAP
}


def main():
    choice = int(input(CHOOSE_SORTER))
    size = 100
    mylist = [i for i in range(1, size + 1)]

    speed = 5
    alg = CHOICE[choice](mylist)
    random.shuffle(mylist)
    anim = AlgAnimation(alg, speed)
    anim.show()


if __name__ == '__main__':
    main()

