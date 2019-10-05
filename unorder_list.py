class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, newnext):
        self.next = newnext


temp = Node(20)
print(temp.getData())


class Unorderedlist:
    def __init__(self, tail=None):
        self.head = None
        self.tail = tail

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    # def append(self, item):
    #     self.add(item)
    #     previous, current = self.head, self.head.getNext()
    #     while current != None:
    #         previous.setData(current.getData())
    #         previous, current = current, current.getNext()
    #     previous.setData(item)

    def append(self, item):
        temp = Node(item)
        previous, current = None, self.head
        while current != None:
            previous, current = current, current.getNext()
        temp.setNext(current)
        previous.setNext(temp)

    def index(self, item):
        cache = {}
        current = self.head
        count = 0
        while current != None:
            cache[current.getData()] = count
            current = current.getNext()
            count += 1
            if item in cache:
                return cache[item]
        return "Index error, item not in List"

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        while current != None:
            if current.getData() == item:
                return True
            current = current.getNext()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        while current != None:
            if current.getData() == item:
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                break
            previous, current = current, current.getNext()

    def pop(self, pos):
        previous, current = None, self.head
        while current != None:
            if self.index(current.getData()) == pos:
                item = current.getData()
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                break
            previous, current = current, current.getNext()
        return item

    def __str__(self):
        output = ""
        current = self.head
        while current != None:
            output += str(current.getData())
            current = current.getNext()

        return output


mylist = Unorderedlist()
mylist.add(8)
mylist.add(7)
mylist.add(6)
mylist.add(5)
mylist.add(4)
mylist.add(3)
mylist.append(9)
mylist.append(10)

print(mylist)
print(mylist.pop(0))
print(mylist)

