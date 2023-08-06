class Node:
   def __init__(self, value):
      self.value = value
      self.next = None

class LinkedList:
   def __init__(self, head=None):
      self.head = head

   def append(self, new_node):
      current = self.head
      if current:
         while current.next:
            current = current.next
         current.next = new_node
      else:
         self.head = new_node

   def delete(self, value):
      """Delete the first node with a given value."""
      current = self.head
      if current.value == value:
         self.head = current.next
      else:
         while current:
            if current.value == value:
               break
            prev = current
            current = current.next
         if current == None:
            return
         prev.next = current.next
         current = None

   def insert(self, new_element, position):
      """Insert a new node at the given position.
      Assume the first position is "1".
      Inserting at position 3 means between
      the 2nd and 3rd elements."""
      count = 1
      current = self.head
      if position == 1:
         new_element.next = self.head
         self.head = new_element
      while current:
         if count + 1 == position:
            new_element.next = current.next
            current.next = new_element
            return
         else:
            count += 1
            current = current.next
         # break
      pass

   def print(self):
      current = self.head
      while current:
         print(current.value)
         current = current.next


arr = [5, 7, 2, 4, 6, 1, 3]
list1 = LinkedList()
list1.head = Node(arr[0])

e2 = Node(31)
e3 = Node(78)
# Link first Node to second node
list1.head.next = e2

# Link second Node to third node
e2.next = e3
e4 = Node(47)
list1.insert(e4, 8)

list1.print()
