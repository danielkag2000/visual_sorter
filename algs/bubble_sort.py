from typing import List
from algs.basic_sort import BasicSort


class BubbleSort(BasicSort):
    def __init__(self, array: List[int]):
        super().__init__(array)

    def calc_all_steps(self):
        steps = list()  # type: List[int]
        steps.append(self.array.copy())

        n = len(self.array)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    steps.append(self.array.copy())
        return steps

