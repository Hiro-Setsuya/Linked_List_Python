class Node: 
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = None

    def append(self, item):
        # Corrected from Item to Node
        new_item = Node(item.title, item.content)
        if self.head is None:
            self.head = new_item
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_item

    def delete(self, index):
        if self.head is None:
            print("List is empty")
            return

        if index == 1:
            print(f"Deleted: {self.head.title}")
            self.head = self.head.next
            return

        temp = self.head
        current_index = 1
        prev = None

        while temp is not None:
            if current_index == index:
                print(f"Deleted: {temp.title}")
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next
            current_index += 1

        print("Invalid index. Item not found.")

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        index = 1
        while temp is not None:
            print(f"{index}. Title: {temp.title}")
            print(f"   Content: {temp.content}")
            temp = temp.next
            index += 1

    def search(self, keyword):
        temp = self.head
        found = False
        index = 1
        while temp is not None:
            if keyword.lower() in temp.title.lower() or keyword.lower() in temp.content.lower():
                print(f"{index}. Title: {temp.title}")
                print(f"   Content: {temp.content}")
                found = True
            temp = temp.next
            index += 1

        if not found:
            print("No matching items found")
