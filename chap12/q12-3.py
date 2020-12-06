'''
・酒井さんのudemyアルゴリズムコースのHeapを参考に作成
・方針としてはMaxheapを用いて、要素数はKを超えないように作成。
・K番目に小さい値が常にheapの最大になるように保持する。
・heapを用いているのでO(NlogN)となっているはず。
・どう出力するのが正解かわからなかったので、K〜N個まで追加した時の
　K番目に小さい値をansのリストで保持
'''

import sys
from typing import Optional


class MaxiHeap(object):

    def __init__(self) -> None:
        self.heap = [sys.maxsize]
        self.current_size = 0

    def parent_index(self, index: int) -> int:
        return index // 2

    def left_child_index(self, index: int) -> int:
        return 2 * index

    def right_child_index(self, index: int) -> int:
        return (2 * index) + 1

    def swap(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_up(self, index: int) -> None:
        while self.parent_index(index) > 0:
            if self.heap[index] > self.heap[self.parent_index(index)]: # min→maxで変更
                self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def push(self, value: int) -> None:
        self.heap.append(value)
        self.current_size += 1
        self.heapify_up(self.current_size)

    def max_child_index(self, index: int) -> int:
        if self.right_child_index(index) > self.current_size:
            return self.left_child_index(index)
        else:
            if (self.heap[self.left_child_index(index)] > # min→maxで変更
                self.heap[self.right_child_index(index)]):
                return self.left_child_index(index)
            else:
                return self.right_child_index(index)

    def heapify_down(self, index: int) -> None:
        while self.left_child_index(index) <= self.current_size:
            max_child_index = self.max_child_index(index)
            if self.heap[index] < self.heap[max_child_index]: # min→maxで変更
                self.swap(index, max_child_index)
            index = max_child_index

    def pop(self) -> Optional[int]:
        if len(self.heap) == 1:
            return

        root = self.heap[1]
        data = self.heap.pop()
        if len(self.heap) == 1:
            return root

        # [-x, 5, 6, 2, 9, 13, 11]
        self.heap[1] = data
        self.current_size -= 1
        self.heapify_down(1)
        return root
    
    def current_max_val(self) -> Optional[int]: # この問題用に追加
        if len(self.heap) == 1:
            return
        else:
            return self.heap[1]


def func(list_a: list, K: int) -> list:
    N = len(list_a)
    ans = []
    max_heap = MaxiHeap()

    for i, ai in enumerate(list_a):
        if i < K-1:
            max_heap.push(ai)
        elif i == K-1:
            max_heap.push(ai)
            # 現在の最大値を追加
            ans.append(max_heap.current_max_val())
        else:
            if ai >= max_heap.current_max_val():
                # 現在の最大値を追加
                ans.append(max_heap.current_max_val())
            else:
                max_heap.pop()
                max_heap.push(ai)
                ans.append(max_heap.current_max_val())
        
    return ans


if __name__ == '__main__':
    list_a = [5, 3, 8, 4, 9, 1, 7]
    K = 3
    print('answer: ', func(list_a, K))
