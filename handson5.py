# -*- coding: utf-8 -*-
"""HandsOn5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mBlc6509qrjeTCSirO63SUaPYX1KsU0y
"""

class MinHeap:
  def __init__(self):
    self.heap=[]
  def parent(self, ind):
    return (ind-1)>>1
  def left_child(self, ind):
    return (ind<<1)+1
  def right_child(self, ind):
    return (ind<<1)+2
  def has_parent(self, index):
    return index>0
  def build_min_heap(self, elements):
    self.heap=elements
    for i in reversed(range(len(self.heap)//2)):
      self.heapify(i)

  def heapify(self, ind):
    small=ind
    left=self.left_child(ind)
    right=self.right_child(ind)

    if left<len(self.heap) and self.heap[left]<self.heap[small]:
      small=left
    if right<len(self.heap) and self.heap[right]<self.heap[small]:
      small=right
    if small!=ind:
      self.heap[ind],self.heap[small]=self.heap[small],self.heap[ind]
      self.heapify(small)

  def pop(self):
    if not self.heap:
      raise IndexError("Pop from an empty heap")
    root_value=self.heap[0]
    last_value=self.heap.pop()
    if self.heap:
      self.heap[0]=last_value
      self.heapify(0)
    return root_value

  def peek(self):
    if not self.heap:
      raise IndexError("Peek from an empty heap")
    return self.heap[0]
  def __str__(self):
    return str(self.heap)


if __name__ == "__main__":
  heap=MinHeap()
  elements=[8, 51, 32, 3, 81, 7]
  heap.build_min_heap(elements)
  print("Built Min Heap:", heap)
  print("Pop from heap:", heap.pop())
  print("Heap after pop:", heap)
  print("Peek at root:", heap.peek())