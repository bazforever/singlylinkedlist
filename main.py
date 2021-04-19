

class linkedListNode:
   def __init__(self, value =0, nextNode = 0):
       self.value = value
       self.nextNode = nextNode

class linkdedList:
    def __init__(self):
        self.head= 0

    def insert(self, value):
        node = linkedListNode(value)
        if self.head :
            currentNode = self.head
            while currentNode.nextNode:
               currentNode = currentNode.nextNode
            currentNode.nextNode = node

        else: self.head = node



    def printLinkdedList(self):
        currentNode = self.head

        while currentNode:
            print(currentNode.value),
            currentNode = currentNode.nextNode


#1538,48
node1 = linkdedList()
node1.insert(1)
node1.insert(4)
node1.insert(7)
node1.insert(9)
node1.printLinkdedList()








































































