class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """在链表末尾添加一个节点"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_list(self):
        """将单向链表转换为 Python 列表"""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    @staticmethod
    def from_list(values):
        """通过 Python 列表创建单向链表"""
        sll = SinglyLinkedList()
        for value in values:
            sll.append(value)
        return sll


def merge_linked_lists(ll1, ll2):
    temp = Node(0)
    current = temp
    head1 = ll1.head
    head2 = ll2.head
    while head1 and head2:
        if head1.value < head2.value:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    current.next = head1 if head1 else head2
    result = SinglyLinkedList()
    result.head = temp.next
    return result


if __name__ == '__main__':
    list1 = SinglyLinkedList.from_list([1, 3, 5, 7])
    list2 = SinglyLinkedList.from_list([2, 4, 6, 8])
    merge_list = merge_linked_lists(list1, list2).to_list()
    print(merge_list)
