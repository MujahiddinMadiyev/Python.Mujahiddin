{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6ffa289b",
   "metadata": {},
   "source": [
    "# Homeworks"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4104cca9",
   "metadata": {},
   "source": [
    "### 1. Modify String with Underscores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "ebe8dd0e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "abc_abc_abc_dea_bcd_efa_bcd_efg\n"
     ]
    }
   ],
   "source": [
    "txt = \"abcabcabcdeabcdefabcdefg\"\n",
    "result = \"\"\n",
    "count = 0\n",
    "for char in txt:\n",
    "    result += char\n",
    "    if result[-1] == \"_\":\n",
    "        continue \n",
    "    count += 1\n",
    "    if count == 3:\n",
    "        result += \"_\"\n",
    "        count = 0\n",
    "print(result.rstrip(\"_\")) \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "37cef16b",
   "metadata": {},
   "source": [
    "### 2. Integer Squares Exercise"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a553a754",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "4\n",
      "9\n",
      "16\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "\n",
    "for i in range(n):\n",
    "    print(i ** 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "55541351",
   "metadata": {},
   "source": [
    "### 3. Loop-Based Exercises\n",
    "Exercise 1: Print first 10 natural numbers using a while loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dbeed6df",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "i = 1\n",
    "while i <= 10:\n",
    "    print(i)\n",
    "    i += 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "437a84a2",
   "metadata": {},
   "source": [
    "### Exercise 2: Print the following pattern"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b15ac68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 \n",
      "1 2 \n",
      "1 2 3 \n",
      "1 2 3 4 \n",
      "1 2 3 4 5 \n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 6):\n",
    "    for j in range(1, i + 1):\n",
    "        print(j, end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1e7d7f18",
   "metadata": {},
   "source": [
    "### Exercise 3: Calculate sum of all numbers from 1 to a given number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "50cdfae3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum is: 55\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"Enter number: \"))\n",
    "total = sum(range(1, n + 1))\n",
    "print(\"Sum is:\", total)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7c7c49ea",
   "metadata": {},
   "source": [
    "### Exercise 4: Print multiplication table of a given number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6469047c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"Enter a number: \"))\n",
    "for i in range(1, 11):\n",
    "    print(n * i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "36ca2ec3",
   "metadata": {},
   "source": [
    "### Exercise 5: Display numbers from a list using a loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5ea2a242",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "75\n",
      "150\n",
      "145\n"
     ]
    }
   ],
   "source": [
    "numbers = [12, 75, 150, 180, 145, 525, 50]\n",
    "for num in numbers:\n",
    "    if num == 75 or num == 150 or num == 145:\n",
    "        print(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "933a5a27",
   "metadata": {},
   "source": [
    "### Exercise 6: Count the total number of digits in a number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "32269908",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total digits: 5\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a number: \"))\n",
    "digit_count = len(str(num))\n",
    "print(\"Total digits:\", digit_count)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "41e35c64",
   "metadata": {},
   "source": [
    "### Exercise 7: Print reverse number pattern"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8ebf66c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 4 5 \n",
      "1 2 3 4 \n",
      "1 2 3 \n",
      "1 2 \n",
      "1 \n"
     ]
    }
   ],
   "source": [
    "for i in range(5, 0, -1):\n",
    "    for j in range(1, i + 1):\n",
    "        print(j, end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "911223d3",
   "metadata": {},
   "source": [
    "### Exercise 8: Print list in reverse order using a loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "50f02599",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "50\n",
      "40\n",
      "30\n",
      "20\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "list1 = [10, 20, 30, 40, 50]\n",
    "for num in reversed(list1):\n",
    "    print(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "304f035a",
   "metadata": {},
   "source": [
    "### Exercise 9: Display numbers from -10 to -1 using a for loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "8d5b1495",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-10\n",
      "-9\n",
      "-8\n",
      "-7\n",
      "-6\n",
      "-5\n",
      "-4\n",
      "-3\n",
      "-2\n",
      "-1\n"
     ]
    }
   ],
   "source": [
    "for num in range(-10, 0):\n",
    "    print(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3ffa1241",
   "metadata": {},
   "source": [
    "### Exercise 10: Display message “Done” after successful loop execution"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "77e3354d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "Done!\n"
     ]
    }
   ],
   "source": [
    "for i in range(5):\n",
    "    print(i)\n",
    "print(\"Done!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9e099cb5",
   "metadata": {},
   "source": [
    "### Exercise 11: Print all prime numbers within a range"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "7056084e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "29\n",
      "31\n",
      "37\n",
      "41\n",
      "43\n",
      "47\n"
     ]
    }
   ],
   "source": [
    "start, end = 25, 50\n",
    "\n",
    "for num in range(start, end + 1):\n",
    "    for i in range(2, num):\n",
    "        if num % i == 0:\n",
    "            break\n",
    "    else:\n",
    "        print(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ce9c3ceb",
   "metadata": {},
   "source": [
    "### Exercise 12: Display Fibonacci series up to 10 terms"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "215a0e2f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1 1 2 3 5 8 13 21 34 \n"
     ]
    }
   ],
   "source": [
    "a, b = 0, 1\n",
    "for _ in range(10):\n",
    "    print(a, end=\" \")\n",
    "    a, b = b, a + b\n",
    "print()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8bffb03a",
   "metadata": {},
   "source": [
    "### Exercise 13: Find the factorial of a given number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "1391cec7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5! = 120\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"Enter a number: \"))\n",
    "factorial = 1\n",
    "for i in range(1, n + 1):\n",
    "    factorial *= i\n",
    "print(f\"{n}! = {factorial}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "31382803",
   "metadata": {},
   "source": [
    "### 4. Return Uncommon Elements of Lists"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "79b0d2e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 2, 5]\n"
     ]
    }
   ],
   "source": [
    "list1 = [1, 1, 2, 3, 4, 2]\n",
    "list2 = [1, 3, 4, 5]\n",
    "result = [num for num in list1 if num not in list2] + [num for num in list2 if num not in list1]\n",
    "print(result)"
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
