from typing import List
from algs.basic_sort import BasicSort


class MergeSort(BasicSort):
    def __init__(self, array: List[int]):
        super().__init__(array)

    def calc_all_steps(self):
        steps = list()  # type: List[int]
        steps.append(self.array.copy())
        steps.extend([step for step in self._merge_sort(0, len(self.array))])
        return steps

    def _merge_sort(self, start: int, end: int):
        if end - start > 1:
            middle = (start + end) // 2

            yield from self._merge_sort(start, middle)
            yield from self._merge_sort(middle, end)

            # Merge
            left = self.array[start:middle]
            right = self.array[middle:end]

            i = j = 0
            k = start

            # Copy data to temp arrays
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.array[k] = left[i]
                    i += 1
                else:
                    self.array[k] = right[j]
                    j += 1
                yield self.array.copy()
                k += 1

            # Check the leftovers
            while i < len(left):
                self.array[k] = left[i]
                i += 1
                k += 1
                yield self.array.copy()

            while j < len(right):
                self.array[k] = right[j]
                j += 1
                k += 1
                yield self.array.copy()
