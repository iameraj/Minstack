import random
import os


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))

        else:
            self.min_stack.append(val)

        print("\nStack: ", self.stack)
        print("Mins : ", self.min_stack)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

        if self.min_stack:
            self.min_stack.pop()

        print("\nStack: ", self.stack)
        print("Mins : ", self.min_stack)

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]


if __name__ == "__main__":
    os.system("clear")
    print("-- Minstack ", "-" * 10)

    obj = MinStack()
    while True:
        choice = input("\nPush(default,1) or pop(0)?: ")
        os.system("clear")
        print("-- Minstack ", "-" * 10)
        if choice == "pop" or choice == "0":
            obj.pop()
        else:
            num = random.randint(0, 100)
            obj.push(num)
        print("Top of the stack: ", obj.top())
        print("Min num in stack: ", obj.getMin())
