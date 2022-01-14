from typing import List
from algs.basic_sort import BasicSort


class InsertionSort(BasicSort):
    def __init__(self, array: List[int]):
        super().__init__(array)

    def calc_all_steps(self):
        steps = list()  # type: List[int]
        steps.append(self.array.copy())

        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
                steps.append(self.array.copy())
            self.array[j+1] = key
            steps.append(self.array.copy())
        return steps
