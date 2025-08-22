import json

class Node:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None

class ContactBook:
    def __init__(self):
        self.head = None

    def insert(self, name, phone):
        new_node = Node(name, phone)
        if not self.head or name.lower() < self.head.name.lower():
            new_node.next = self.head
            self.head = new_node
            return
        cur = self.head
        while cur.next and cur.next.name.lower() < name.lower():
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node

    def search(self, name):
        cur = self.head
        while cur:
            if cur.name.lower() == name.lower():
                return cur.phone
            cur = cur.next
        return None

    def update(self, name, new_phone):
        cur = self.head
        while cur:
            if cur.name.lower() == name.lower():
                cur.phone = new_phone
                return True
            cur = cur.next
        return False

    def delete(self, name):
        cur = self.head
        prev = None
        while cur:
            if cur.name.lower() == name.lower():
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev = cur
            cur = cur.next
        return False

    def display(self):
        cur = self.head
        while cur:
            print(cur.name, cur.phone)
            cur = cur.next

    def save(self, filename):
        data = []
        cur = self.head
        while cur:
            data.append({"name": cur.name, "phone": cur.phone})
            cur = cur.next
        with open(filename, "w") as f:
            json.dump(data, f)

    def load(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.head = None
            for contact in sorted(data, key=lambda x: x["name"].lower(), reverse=True):
                self.insert(contact["name"], contact["phone"])
        except FileNotFoundError:
            pass

book = ContactBook()
book.load("contacts.json")
book.insert("Alice", "12345")
book.insert("Charlie", "67890")
book.insert("Bob", "54321")
book.display()
print("Search Bob:", book.search("Bob"))
book.update("Alice", "11111")
book.delete("Charlie")
book.display()
book.save("contacts.json")
