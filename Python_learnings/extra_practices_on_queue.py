#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: extra_practices_on_queue.py
# Created: Sunday, 24th July 2022 11:41:25 pm
# Author: Azwad Aziz (azwad.a02@hotmail.com)
# -----
# Last Modified: Sunday, 24th July 2022 11:41:35 pm
# Modified By: Azwad Aziz (azwad.a02@hotmail.com)
# -----
# Copyright (c) 2022 Dreams
###


class Array_Queue:

  def __init__(self, array, start, size):
    self.array = array
    self.start = start
    self.size = size

  def enqueue(self, elem):
    if self.size < len(self.array):

      idx = (self.start + self.size) % len(self.array)
      self.array[idx] = elem

    else:
      print("No space available")

  def dequeue(self):

    if self.size > 0:
      x = self.array[self.start]
      self.array[self.start] = None
      self.start = (self.start+1) % len(self.array)
      self.size -= 1
      return x

    else:
      print("No item to dequeue")

  def print_array(self):
    print(self.array)


class Node:
  def __init__(self, elem, next):
    self.elem = elem
    self.next = next


class List_Queue:

  def __init__(self, head):
    self.head = head

  def enqueue(self, elem):
    n = Node(elem, None)

    if self.head == None:
      self.head = n

    else:
      h = self.head
      while(h.next != None):
        h = h.next

      h.next = n

  def dequeue(self):
    if self.head == None:
      print("No item to dequeue")

    else:
      h = self.head
      self.head = self.head.next
      h.next = None

      return h

  def print_list(self):
    h = self.head
    while(h != None):
      print(h.elem)
      h = h.next


array_1 = [50, None, None, 10, 20, 30, 40]

# object_1 = Array_Queue(array_1,3,5)
# object_1.print_array()
# object_1.dequeue()
# object_1.print_array()
# object_1.enqueue(60)
# object_1.print_array()


def create_list(array_1):
  head = Node(array_1[0], None)
  n1 = head
  i = 1
  while(i < len(array_1)):
    n2 = Node(array_1[i], None)
    n1.next = n2
    n1 = n2
    i += 1

  return head

# list_1 = create_list(array_1)
# object_2 = List_Queue(list_1)
# object_2.print_list()
# object_2.enqueue(60)
# object_2.print_list()
# object_2.dequeue()
# object_2.print_list()
