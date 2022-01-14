from typing import List


class BasicSorter(object):
    def __init__(self, array: List[int]):
        self.array = array
        self._array_copy = array.copy()

    def calc_all_steps(self) -> List[int]:
        raise NotImplementedError()

    def sort_generator(self):
        for step in self.calc_all_steps():
            yield step

    def sort(self) -> List[int]:
        for _ in self.sort_generator():
            pass
        return self._array.copy()

    def reset(self):
        self._array = self._array_copy.copy()
