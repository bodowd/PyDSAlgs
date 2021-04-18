class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# test cases
# s = Stack()
# print(s.isEmpty()) # True
# s.push(4) # [4]
# s.push('dog') # [4, 'dog']
# print(s.peek())
# s.push(True)
# print(s.peek()) # True
# s.pop()
# print(s.peek()) # dog
# print(s.size())

# reverse a string with stack
rev_stack = Stack()
test_str = 'Jump'
for i in test_str:
    rev_stack.push(i)
result = ""
while not rev_stack.isEmpty():
    result += rev_stack.pop()
print(result)

