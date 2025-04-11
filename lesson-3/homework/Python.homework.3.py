{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3c054d76",
   "metadata": {},
   "source": [
    "# Homework: List and Tuple Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "16a6f8e3",
   "metadata": {},
   "source": [
    "### 1. Create and Access List Elements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f4f68fe3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "peach\n"
     ]
    }
   ],
   "source": [
    "Fruits = ['apple', 'mango', 'peach', 'banana', 'orange']\n",
    "print(Fruits[2])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fef91e5d",
   "metadata": {},
   "source": [
    "### 2. Concatenate Two Lists"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6ca23632",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "num1 = [1, 2, 3]\n",
    "num2 = [4, 5, 6]\n",
    "num3 = num1 + num2\n",
    "print(num3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d34cb4f6",
   "metadata": {},
   "source": [
    "### 3. Extract Elements from a List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1f092862",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[15, 30, 45]\n"
     ]
    }
   ],
   "source": [
    "numbers = [15, 20, 25, 30, 35, 40, 45]\n",
    "first = numbers[0]\n",
    "middle = numbers[len(numbers) // 2]\n",
    "last = numbers[-1]\n",
    "new_list = [first, middle, last]\n",
    "print(new_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e736767",
   "metadata": {},
   "source": [
    "### 4. Convert List to Tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3869b87c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('interstellar', 'the last day', 'the day after tomorrow', 'moonfall', 'inception')\n"
     ]
    }
   ],
   "source": [
    "movies = ['interstellar', 'the last day', 'the day after tomorrow', 'moonfall', 'inception']\n",
    "movies_tuple = tuple(movies)\n",
    "print(movies_tuple)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "42025543",
   "metadata": {},
   "source": [
    "### 5. Check Element in a List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "dc023301",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Paris\n"
     ]
    }
   ],
   "source": [
    "cities = [\"London\", \"Tokyo\", \"New York\", \"Berlin\", \"Paris\", \"Dubai\"]\n",
    "index = cities.index(\"Paris\")\n",
    "print(cities[index])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25f9c3fc",
   "metadata": {},
   "source": [
    "### 6. Duplicate a List Without Using Loops"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "62c8e37e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "list1 = [1, 2, 3, 4, 5]\n",
    "list2 = list1 * 2\n",
    "print(list2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3aaf4b6",
   "metadata": {},
   "source": [
    "### 7. Swap First and Last Elements of a List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "3752e786",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[50, 20, 30, 40, 10]\n"
     ]
    }
   ],
   "source": [
    "numbers = [10, 20, 30, 40, 50]\n",
    "numbers[0], numbers[-1] = numbers[-1], numbers[0]\n",
    "print(numbers)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "73d292b3",
   "metadata": {},
   "source": [
    "### 8. Slice a Tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ff60c0f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(4, 5, 6, 7, 8)\n"
     ]
    }
   ],
   "source": [
    "numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)\n",
    "sliced_tuple = numbers_tuple[3:8]\n",
    "print(sliced_tuple)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "067c7ab7",
   "metadata": {},
   "source": [
    "### 9. Count Occurrences in a List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "3dba8919",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "colors = ['blue', 'red', 'blue']\n",
    "count1 = colors.count('blue')\n",
    "print(count1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e91ce632",
   "metadata": {},
   "source": [
    "### 10. Find the Index of an Element in a Tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "84676888",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "tuple = ('tiger', 'lion', 'bear')\n",
    "index = tuple.index('lion')\n",
    "print(index)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5b549800",
   "metadata": {},
   "source": [
    "### 11. Merge Two Tuples"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "8eacb440",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)\n"
     ]
    }
   ],
   "source": [
    "tuple1 = (1, 2, 3, 4, 5)\n",
    "tuple2 = (6, 7, 8, 9, 10)\n",
    "merged_tuple = tuple1 + tuple2\n",
    "print(merged_tuple)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e99e95e2",
   "metadata": {},
   "source": [
    "### 12. Find the Length of a List and Tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "8737ff19",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "my_list = [10, 20, 30, 40, 50]\n",
    "my_tuple = (1, 2, 3, 4, 5, 6)\n",
    "print(len(my_list))\n",
    "print(len(my_tuple))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d5fa756f",
   "metadata": {},
   "source": [
    "### 13. Convert Tuple to List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "e45efe4c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "tuple_numbers = (1, 2, 3, 4, 5)\n",
    "list_number = list(tuple_numbers)\n",
    "print(list_number)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7451ac5e",
   "metadata": {},
   "source": [
    "### 14. Find Maximum and Minimum in a Tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "f0d54d0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "nice_tuples = (1, 2, 3, 4, 5)\n",
    "print(max(nice_tuples))\n",
    "print(min(nice_tuples))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2d892de1",
   "metadata": {},
   "source": [
    "### 15. Reverse a Tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "29488c20",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('elderberry', 'date', 'cherry', 'banana', 'apple')\n"
     ]
    }
   ],
   "source": [
    "words_tuple = (\"apple\", \"banana\", \"cherry\", \"date\", \"elderberry\")\n",
    "reversed_tuple = words_tuple[::-1]\n",
    "print(reversed_tuple)\n"
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
