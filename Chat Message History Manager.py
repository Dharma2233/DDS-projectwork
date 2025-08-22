import time
from collections import deque

class Message:
    def __init__(self, text):
        self.text = text
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

class ChatManager:
    def __init__(self):
        self.queue = deque()
        self.undo_stack = []
        self.redo_stack = []

    def send_message(self, text):
        msg = Message(text)
        self.queue.append(msg)
        self.undo_stack.append(msg)
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            msg = self.undo_stack.pop()
            self.redo_stack.append(msg)
            self.queue.remove(msg)

    def redo(self):
        if self.redo_stack:
            msg = self.redo_stack.pop()
            self.queue.append(msg)
            self.undo_stack.append(msg)

    def show_messages(self):
        for m in self.queue:
            print(m.timestamp, m.text)

chat = ChatManager()
chat.send_message("Hello")
chat.send_message("How are you?")
chat.show_messages()
chat.undo()
print("After Undo:")
chat.show_messages()
chat.redo()
print("After Redo:")
chat.show_messages()
