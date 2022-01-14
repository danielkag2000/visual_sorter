from typing import List


class BasicSort(object):
    def __init__(self, array: List[int]):
        self.array = array
        self._array_copy = array.copy()

    def calc_all_steps(self) -> List[int]:
        raise NotImplementedError()

    def sort_generator(self):
        for step in self.calc_all_steps():
            yield step

    def sort(self) -> List[int]:
        return self.calc_all_steps()[-1]

    def reset(self):
        self.array = self._array_copy.copy()
