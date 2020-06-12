class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):

        if self.head == None:
            return "Linked List is empty"

        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:

            self.head = Node(value)
            self.tail = self.head

        else:

            node = self.tail
            node.next = Node(value)
            node.next.previous = node
            self.tail = node.next
        self.length += 1


    def get_length(self):
        return self.length


    def get_unique_linked_list(self):
        unique_values = set()
        unique_linked_list = LinkedList()
        node = self.head

        while node:
            if node.value not in unique_values:
                unique_linked_list.append(node)
                unique_values.add(node.value)
            node = node.next

        return unique_linked_list


    def get_unique_values(self):
        unique_values = set()
        node = self.head

        while node:

            unique_values.add(node.value)
            node = node.next

        return unique_values


    def delete_node(self, node):

        if node == self.head:
            if self.length == 1:
                self.head = None
                node.next = None
                node.previous = None

            else:
                self.head = node.next
                self.head.previous = None
                node.next = None

        elif node == self.tail:
            self.tail = node.previous
            self.tail.next = None
            node.previous = None

        else:
            node.previous.next = node.next
            node.next.previous = node.previous
            node.next = None
            node.previous = None

        self.length -= 1
        return


def union(llist_1, llist_2):

    union_linked_list = llist_1.get_unique_linked_list()
    unique_values = llist_1.get_unique_values()

    node = llist_2.head

    while node:

        if node.value not in unique_values:
            union_linked_list.append(node)
            unique_values.add(node.value)

        node = node.next

    return union_linked_list

def intersection(llist_1, llist_2):


    intersection_linked_list = llist_1
    unique_values = llist_2.get_unique_values()

    node = intersection_linked_list.head

    while node:
        new_node = node.next

        if node.value in unique_values: #<-- keep node because it is present in both linked lists
            unique_values.remove(node.value) #<-- remove value from unique_values to avoid duplicate values in output linked list
        else:
            intersection_linked_list.delete_node(node)

        node = new_node

    return intersection_linked_list


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1,linked_list_2)) #<-- return: [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11]
print()
print(intersection(linked_list_1,linked_list_2)) #<-- return: [4, 6, 21]
print()
print()
print()


# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3,linked_list_4)) # <-- return: [3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21]
print()
print(intersection(linked_list_3,linked_list_4)) #<-- return: Linked List empty, since the intersection of these 2 lists is none
print()
print()
print()


# Test case 3
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3,linked_list_4)) #<-- return: [1, 7, 8, 9, 11, 21]
print()
print(intersection(linked_list_3,linked_list_4)) #<-- return: Linked List empty, since the first linked list is empty, there is no intersection.
