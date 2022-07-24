input = "][{()}]"


class Array_Stack:

  def __init__(self, input):
    array = [None]*(len(input))
    self.array = array
    self.input = input
    self.top = -1

  def push(self, val):
    self.array[self.top+1] = val
    self.top += 1

  def pop(self):
    x = self.array[self.top]
    self.array[self.top] = None

    self.top -= 1

    return x

  def printStack(self):
    temp = self.top
    i = temp
    while(i != -1):
      print(self.array[i], end="   ")
      i -= 1

  def peak(self):
    return self.array[self.top]


def check_bracket_array(input):
  obj1 = Array_Stack(input)
  flag = True

  for i in input:
    if(i == "[" or i == "{" or i == "("):
      obj1.push(i)

    elif(i == "]" or i == "}" or i == ")"):

      if obj1.top == -1:
        flag = False

        break

      else:

        x = obj1.pop()

        if ((i == ")" and x == "(") or (i == "}" and x == "{") or (i == "]" and x == "[")):
          continue
        else:
          flag = False
          break

  if obj1.top > -1:

    flag = False

  if flag == True:
    print("This expression is correct")
  else:
    print("This expression is incorrect")


class Node:
  def __init__(self, element, next):
    self.element = element
    self.next = next


class List_Stack:

  def __init__(self):

    self.head = Node(None, None)
    self.top = self.head

  def push(self, value):
    if self.head.element == None:
      self.head.element = value

    else:

      n1 = Node(value, None)
      self.top.next = n1
      self.top = n1

  def pop(self):
    if self.head == self.top:
      x = self.head.element
      self.head.element = None

    else:
      x = self.top.element
      h = self.head
      while(h.next != self.top):
        h = h.next
      h.next = None
      self.top = h

    return x

  def peak(self):
    return self.top.element


def check_bracket_list(input):
  obj1 = List_Stack()
  flag = True

  for i in input:
    if(i == "[" or i == "{" or i == "("):
      obj1.push(i)

    elif(i == "]" or i == "}" or i == ")"):

      if obj1.top.element == None:
         flag = False

         break

      else:

        x = obj1.pop()

        if ((i == ")" and x == "(") or (i == "}" and x == "{") or (i == "]" and x == "[")):
          continue
        else:
          flag = False
          break

  if obj1.top.element != None:

    flag = False

  if flag == True:
    print("This expression is correct")
  else:
    print("This expression is incorrect")


check_bracket_array(input)
check_bracket_list(input)
