import random
class Node:

    def __init__ (self, data):
        self.data = data
        self.next = None


class LinkedList:


    def __init__ (self):
        self.head = None


    def reverse (self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


    def add (self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def printLl (self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print('\n')

    def findNum(self, num):
        counter = 0
        temp = self.head
        while temp:
            if counter == num - 1:
                return temp.data
            counter += 1
            temp = temp.next


    def llMaker(self):
        for i in range(random.randint(6,11)):
            self.add(i)

llist = LinkedList()
llist.llMaker()

num = int(input())
llist.printLl()
llist.reverse()
print(llist.findNum(num))
llist.printLl()