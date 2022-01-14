from typing import List
from algs.basic_sort import BasicSort


class QuickSort(BasicSort):
    def __init__(self, array: List[int]):
        super().__init__(array)

    def calc_all_steps(self):
        steps = list()  # type: List[int]
        steps.append(self.array.copy())
        steps.extend([step for step in self._quick_sort(0, len(self.array) - 1)])
        return steps

    def _quick_sort(self, start: int, end: int):
        if start < end:
            # partition
            pivot = self.array[end]
            i = start - 1

            for j in range(start, end):
                if self.array[j] <= pivot:
                    i += 1
                    self.array[i], self.array[j] = self.array[j], self.array[i]
                    yield self.array.copy()
            self.array[i+1], self.array[end] = self.array[end], self.array[i+1]
            yield self.array.copy()
            pi = i + 1
            # end partition

            yield from self._quick_sort(start, pi - 1)
            yield from self._quick_sort(pi + 1, end)
