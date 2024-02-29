from llist import LList, Node, append


def length(lst):
    if lst.head:
        node=lst.head
        counter=1 
        while node.next:
            counter+= 1
            node=node.next
    else:
        counter=0
    print(counter)

def llprint(lst):
    """print a finite linked list"""
    if lst.head:  # same as:  if lst.head is not None
        node = lst.head
        while node.next:
            print(node.val, end=" ")
            node=node.next
        print(node.val)
    else:
        print("empty")



if __name__ == "__main__":
    nums= [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    lst= LList()
    for i in nums:
        append(lst,Node(i))
    llprint(lst)
    length(lst)
        
from genfinite import lst 
print(length(lst))
