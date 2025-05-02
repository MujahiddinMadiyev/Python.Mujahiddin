{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "00ac1917",
   "metadata": {},
   "source": [
    "# Homework:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1d482f30",
   "metadata": {},
   "source": [
    "## Object-Oriented Programming (OOP) Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3eceb327",
   "metadata": {},
   "source": [
    "### 1. Circle Class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cbaa0078",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "class Circle:\n",
    "    def __init__(self, radius):\n",
    "        self.radius = radius\n",
    "\n",
    "    def area(self):\n",
    "        return math.pi * self.radius**2\n",
    "\n",
    "    def perimeter(self):\n",
    "        return 2 * math.pi * self.radius\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2626d447",
   "metadata": {},
   "source": [
    "### 2. Person Class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "18a8de52",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import datetime\n",
    "\n",
    "class Person:\n",
    "    def __init__(self, name, country, dob):  # dob in 'YYYY-MM-DD'\n",
    "        self.name = name\n",
    "        self.country = country\n",
    "        self.dob = datetime.strptime(dob, \"%Y-%m-%d\")\n",
    "\n",
    "    def age(self):\n",
    "        today = datetime.today()\n",
    "        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "81442c78",
   "metadata": {},
   "source": [
    "### 3. Calculator Class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "90bc78c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Calculator:\n",
    "    def add(self, a, b): return a + b\n",
    "    def subtract(self, a, b): return a - b\n",
    "    def multiply(self, a, b): return a * b\n",
    "    def divide(self, a, b): return a / b if b != 0 else \"Division by zero\"\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a2483b91",
   "metadata": {},
   "source": [
    "### 4. Shape and Subclasses"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "63a9a73d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "class Shape:\n",
    "    def area(self): pass\n",
    "    def perimeter(self): pass\n",
    "\n",
    "class Circle(Shape):\n",
    "    def __init__(self, radius): self.radius = radius\n",
    "    def area(self): return math.pi * self.radius ** 2\n",
    "    def perimeter(self): return 2 * math.pi * self.radius\n",
    "\n",
    "class Square(Shape):\n",
    "    def __init__(self, side): self.side = side\n",
    "    def area(self): return self.side ** 2\n",
    "    def perimeter(self): return 4 * self.side\n",
    "\n",
    "class Triangle(Shape):\n",
    "    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c\n",
    "    def perimeter(self): return self.a + self.b + self.c\n",
    "    def area(self):\n",
    "        s = self.perimeter() / 2\n",
    "        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "43366572",
   "metadata": {},
   "source": [
    "### 5. Binary Search Tree Class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "13dbb639",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Node:\n",
    "    def __init__(self, value):\n",
    "        self.value = value\n",
    "        self.left = None\n",
    "        self.right = None\n",
    "\n",
    "class BST:\n",
    "    def __init__(self): self.root = None\n",
    "\n",
    "    def insert(self, value):\n",
    "        def _insert(node, value):\n",
    "            if not node: return Node(value)\n",
    "            if value < node.value:\n",
    "                node.left = _insert(node.left, value)\n",
    "            else:\n",
    "                node.right = _insert(node.right, value)\n",
    "            return node\n",
    "        self.root = _insert(self.root, value)\n",
    "\n",
    "    def search(self, value):\n",
    "        def _search(node, value):\n",
    "            if not node: return False\n",
    "            if value == node.value: return True\n",
    "            return _search(node.left, value) if value < node.value else _search(node.right, value)\n",
    "        return _search(self.root, value)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0c106d69",
   "metadata": {},
   "source": [
    "### 6. Stack Data Structure"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "fe451014",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Stack:\n",
    "    def __init__(self): self.stack = []\n",
    "\n",
    "    def push(self, item): self.stack.append(item)\n",
    "    def pop(self): return self.stack.pop() if self.stack else None\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "71886157",
   "metadata": {},
   "source": [
    "### 7. Linked List Data Structure"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "be87146b",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Node:\n",
    "    def __init__(self, data): self.data = data; self.next = None\n",
    "\n",
    "class LinkedList:\n",
    "    def __init__(self): self.head = None\n",
    "\n",
    "    def insert(self, data):\n",
    "        new_node = Node(data)\n",
    "        new_node.next = self.head\n",
    "        self.head = new_node\n",
    "\n",
    "    def delete(self, key):\n",
    "        temp = self.head\n",
    "        if temp and temp.data == key:\n",
    "            self.head = temp.next\n",
    "            return\n",
    "        prev = None\n",
    "        while temp and temp.data != key:\n",
    "            prev = temp\n",
    "            temp = temp.next\n",
    "        if temp: prev.next = temp.next\n",
    "\n",
    "    def display(self):\n",
    "        temp = self.head\n",
    "        while temp:\n",
    "            print(temp.data, end=\" -> \")\n",
    "            temp = temp.next\n",
    "        print(\"None\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0cf64ee4",
   "metadata": {},
   "source": [
    "### 8. Shopping Cart Class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6146aa87",
   "metadata": {},
   "outputs": [],
   "source": [
    "class ShoppingCart:\n",
    "    def __init__(self): self.items = {}\n",
    "\n",
    "    def add_item(self, name, price, quantity=1):\n",
    "        if name in self.items:\n",
    "            self.items[name]['quantity'] += quantity\n",
    "        else:\n",
    "            self.items[name] = {'price': price, 'quantity': quantity}\n",
    "\n",
    "    def remove_item(self, name):\n",
    "        if name in self.items: del self.items[name]\n",
    "\n",
    "    def total(self):\n",
    "        return sum(item['price'] * item['quantity'] for item in self.items.values())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2cb43399",
   "metadata": {},
   "source": [
    "### 9. Stack with Display"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "58c72361",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Stack:\n",
    "    def __init__(self): self.stack = []\n",
    "\n",
    "    def push(self, item): self.stack.append(item)\n",
    "    def pop(self): return self.stack.pop() if self.stack else None\n",
    "    def display(self): print(self.stack)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8a933754",
   "metadata": {},
   "source": [
    "### 10. Queue Data Structure"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "63c3e7b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Queue:\n",
    "    def __init__(self): self.queue = []\n",
    "\n",
    "    def enqueue(self, item): self.queue.append(item)\n",
    "    def dequeue(self): return self.queue.pop(0) if self.queue else None\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a7ed532d",
   "metadata": {},
   "source": [
    "### 11. Bank Class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "1b30ff07",
   "metadata": {},
   "outputs": [],
   "source": [
    "class BankAccount:\n",
    "    def __init__(self, name, balance=0):\n",
    "        self.name = name\n",
    "        self.balance = balance\n",
    "\n",
    "    def deposit(self, amount): self.balance += amount\n",
    "    def withdraw(self, amount):\n",
    "        if amount <= self.balance:\n",
    "            self.balance -= amount\n",
    "            return True\n",
    "        return False\n",
    "\n",
    "    def get_balance(self): return self.balance\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
