{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c7744808",
   "metadata": {},
   "source": [
    "# Homework:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0895b6f",
   "metadata": {},
   "source": [
    "### 1. def is_leap(year): \"\"\" Determines whether a given year is a leap year."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7bf2ccd1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2000 is a leap year\n"
     ]
    }
   ],
   "source": [
    "year = int(input('enter a year'))\n",
    "if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):\n",
    "    print(f\"{year} is a leap year\")\n",
    "else:\n",
    "    print(f\"{year} is not a leap year\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dfa4a6e0",
   "metadata": {},
   "source": [
    "### 2. Conditional Statements Exercise"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "1e5566b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Weird\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"enter a number\"))\n",
    "if n % 2 != 0:\n",
    "        print(\"Weird\")\n",
    "elif 2 <= n <= 5:\n",
    "        print(\"Not Weird\")\n",
    "elif 6 <= n <= 20:\n",
    "        print(\"Weird\")\n",
    "else:\n",
    "        print(\"Not Weird\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd8f202d",
   "metadata": {},
   "source": [
    "### 3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "375169bc",
   "metadata": {},
   "source": [
    "#### with else-if"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "930a2b7f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[20, 22, 24, 26, 28, 30, 32, 34]\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"enter a number\"))\n",
    "b = int(input(\"enter a number\"))\n",
    "if a % 2 != 0 and b % 2 != 0:\n",
    "    a += 1\n",
    "    b -= 1\n",
    "elif a % 2 != 0:\n",
    "    a += 1\n",
    "elif b % 2 != 0:\n",
    "    b -= 1\n",
    "numbers_even = list(range(a, b + 1, 2))\n",
    "print(numbers_even)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f07d96ed",
   "metadata": {},
   "source": [
    "#### without else-if"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "98592b0b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 12, 14]\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"enter a number\"))\n",
    "b = int(input(\"enter a number\"))\n",
    "if a % 2 != 0:\n",
    "    a += 1\n",
    "if b % 2 != 0:\n",
    "    b -= 1\n",
    "numbers_even = list(range(a, b + 1, 2))\n",
    "print(numbers_even)"
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
