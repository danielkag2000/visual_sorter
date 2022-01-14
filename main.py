import random
from algs.bubble_sort import BubbleSort
from algs.animation import AlgAnimation


def main(size):
    mylist = [i for i in range(1, size+1)]
    speed = 1
    random.shuffle(mylist)
    alg = BubbleSort(mylist)
    anim = AlgAnimation(alg, speed)
    anim.show()


if __name__ == '__main__':
    main(100)

