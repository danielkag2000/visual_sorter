from algs.bubble_sort import BubbleSort
from algs.quick_sort import QuickSort
from algs.heap_sort import HeapSort
from algs.insertion_sort import InsertionSort
from algs.merge_sort import MergeSort

__all__ = ['SORTERS']


class SORTERS(object):
    BUBBLE = BubbleSort
    QUICK = QuickSort
    HEAP = HeapSort
    INSERTION = InsertionSort
    MERGE = MergeSort

