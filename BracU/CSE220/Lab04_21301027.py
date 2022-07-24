class Node:
  def __init__(self, e, n, p):
    self.element = e
    self.next = n
    self.prev = p


class DoublyList:

  def __init__(self, a):
    if type(a) == list:
        head = Node(None, None, None)
        n1 = head
        i = 0
        while(i < len(a)):
            n2 = Node(a[i], None, None)
            n2.prev = n1
            n1.next = n2
            n1 = n2
            i += 1
        n1.next = head
        head.prev = n1
        self.head = head

  # Counts the number of Nodes in the list

  def countNode(self):
    count = 0
    h = self.head.next
    while(h != self.head):
      count += 1
      h = h.next
    return count

  # prints the elements in the list

  def forwardprint(self):
    h = self.head.next
    while (h != self.head):
        if h.next == self.head:
          print(h.element, end=".\n")
        else:
          print(h.element, end=",")

        h = h.next

  # prints the elements in the list backward

  def backwardprint(self):
    h = self.head.prev
    while(h != self.head):
      if h.prev == self.head:
        print(h.element, end=".\n")
      else:

        print(h.element, end=",")
      h = h.prev

  # returns the reference of the at the given index. For invalid index return None.

  def nodeAt(self, idx):
    x = self.countNode()
    if(idx > -1 and idx < x):
      h = self.head.next
      i = 0
      while(i != idx):
        i += 1
        h = h.next
      return h
    else:
      print("Invalid Index")

  # returns the index of the containing the given element. if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    i = 0
    h = self.head.next
    while(h.element != elem):
      h = h.next
      i += 1

    if(i == self.countNode() and h.elemnet != elem):
      i = -1

    return i

  # inserts containing the given element at the given index Check validity of index.

  def insert(self, elem, idx):
    if(idx > -1 and idx <= self.countNode()):
      new = Node(elem, None, None)
      h = self.head
      i = 0
      while(i < idx):
        h = h.next
        i += 1

      new.next = h.next
      new.prev = h
      h.next.prev = new
      h.next = new

    else:
      print("Invalid Index")

  # removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.

  def remove(self, idx):
    if(idx > -1 and idx <= self.countNode()):

      h = self.head
      i = 0
      while(i < idx+1):
        h = h.next
        i += 1

      h.prev.next = h.next
      h.next.prev = h.prev

      rem = h.element

      h = None

      return str(rem)

    else:
      print("Invalid Index")


print("///  Test 01  ///")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1)  # Creates a linked list using the values from the array

h1.forwardprint()  # This should print: 10,20,30,40.
h1.backwardprint()  # This should print: 40,30,20,10.
print(h1.countNode())  # This should print: 4

print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(2)
# This should print: 30. In case of invalid index This will print "index error"
print(myNode.element)

print("///  Test 03  ///")
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index)  # This should print: 3. In case of element that
#doesn't exists in the list this will print -1.

print("///  Test 04  ///")

a2 = [10, 20, 30, 40]
h2 = DoublyList(a2)  # uses the  constructor
h2.forwardprint()  # This should print: 10,20,30,40.

# inserts containing the given element at the given index. Check validity of index.
h2.insert(85, 0)
h2.forwardprint()  # This should print: 85,10,20,30,40.
h2.backwardprint()  # This should print: 40,30,20,10,85.

print()
h2.insert(95, 3)
h2.forwardprint()  # This should print: 85,10,20,95,30,40.
h2.backwardprint()  # This should print: 40,30,95,20,10,80.

print()
h2.insert(75, 6)
h2.forwardprint()  # This should print: 85,10,20,95,30,40,75.
h2.backwardprint()  # This should print: 75,40,30,95,20,10,85.


print("///  Test 05  ///")
a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3)  # uses the constructor
h3.forwardprint()  # This should print: 10,20,30,40,50,60,70.

# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
# This should print: Removed element: 10
print("Removed element: " + h3.remove(0))
h3.forwardprint()  # This should print: 20,30,40,50,60,70.
h3.backwardprint()  # This should print: 70,60,50,40,30,20.
# This should print: Removed element: 50
print("Removed element: " + h3.remove(3))
h3.forwardprint()  # This should print: 20,30,40,60,70.
h3.backwardprint()  # This should print: 70,60,40,30,20.
# This should print: Removed element: 70
print("Removed element: " + h3.remove(4))
h3.forwardprint()  # This should print: 20,30,40,60.
h3.backwardprint()  # This should print: 60,40,30,20.
