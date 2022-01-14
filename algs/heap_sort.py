from typing import List
from algs.basic_sort import BasicSort


class HeapSort(BasicSort):
    def __init__(self, array: List[int]):
        super().__init__(array)

    def calc_all_steps(self):
        steps = list()  # type: List[int]
        steps.append(self.array.copy())
        steps.extend(self._heap_sort())
        return steps

    def _heapify(self, n: int, i: int):
        steps = list()
        largest = i
        left = i * 2 + 1
        right = i * 2 + 2

        if left < n and self.array[largest] < self.array[left]:
            largest = left

        if right < n and self.array[largest] < self.array[right]:
            largest = right

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            steps.append(self.array.copy())

            steps.extend(self._heapify(n, largest))
        return steps

    def _heap_sort(self):
        n = len(self.array)
        steps = list()

        for i in range(n // 2 - 1, -1, -1):
            steps.extend(self._heapify(n, i))

        for i in range(n - 1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            steps.append(self.array.copy())
            self._heapify(i, 0)
        return steps
