{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7e6a16c2",
   "metadata": {},
   "source": [
    "# Python Dictionary and Set Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "294a80ca",
   "metadata": {},
   "source": [
    "## Dictionary Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2b8a35cb",
   "metadata": {},
   "source": [
    "### 1. Sort a Dictionary by Value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "e30a1204",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['age', 'country', 'name']\n",
      "['name', 'country', 'age']\n"
     ]
    }
   ],
   "source": [
    "dictionary_dict = {'name': 'James', 'age': 25, 'country': 'Uzbekistan'}\n",
    "print(sorted(dictionary_dict))\n",
    "print(sorted(dictionary_dict, reverse=True))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0934dcff",
   "metadata": {},
   "source": [
    "### 2. Add a Key to a Dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "d2273dc8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0: 10, 1: 20, '2': 30}\n"
     ]
    }
   ],
   "source": [
    "rais = {0: 10, 1: 20}\n",
    "rais['2'] = 30\n",
    "print(rais)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3208845f",
   "metadata": {},
   "source": [
    "### 3. Concatenate Multiple Dictionaries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "6f093391",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}\n"
     ]
    }
   ],
   "source": [
    "dic1 = {1: 10, 2: 20}\n",
    "dic2 = {3: 30, 4: 40}\n",
    "dic3 = {5: 50, 6: 60}\n",
    "dic1.update(dic2)\n",
    "dic1.update(dic3)\n",
    "print(dic1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e9b6bb92",
   "metadata": {},
   "source": [
    "### 4. Generate a Dictionary with Squares"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5dab8135",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}\n"
     ]
    }
   ],
   "source": [
    "square_dict = {}\n",
    "for x in range(1, 6):\n",
    " square_dict[x] = x * x\n",
    "print(square_dict)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "36fa19e2",
   "metadata": {},
   "source": [
    "### 5. Dictionary of Squares (1 to 15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "5f117c06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}\n"
     ]
    }
   ],
   "source": [
    "square_dict2 = {}\n",
    "for x in range(1, 16):\n",
    " square_dict2[x] = x * x\n",
    "print(square_dict2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1830dca0",
   "metadata": {},
   "source": [
    "## Set Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0bfcfc0d",
   "metadata": {},
   "source": [
    "### 1. Create a Set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "7dbf84e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 4, 5}\n"
     ]
    }
   ],
   "source": [
    "set1 = {1, 2, 3, 4, 5}\n",
    "print(set1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "69a9c7c2",
   "metadata": {},
   "source": [
    "### 2. Iterate Over a Set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "97d62567",
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
      "5\n"
     ]
    }
   ],
   "source": [
    "set2 = {1, 2, 3, 4, 5}\n",
    "for set2 in my_set:\n",
    "    print(set2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bdf690bc",
   "metadata": {},
   "source": [
    "### 3. Add Member(s) to a Set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "0047e66a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Richard', 'Jones', 'Phil', 'Jacob', 'Khan', 'Liam', 'Arthur', 'James'}\n"
     ]
    }
   ],
   "source": [
    "set3 = {'James', 'Arthur', 'Jacob', 'Jones', 'Phil'}\n",
    "set3.update(['Richard', 'Liam', 'Khan'])\n",
    "print(set3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b34af80c",
   "metadata": {},
   "source": [
    "### 4. Remove Item(s) from a Set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "cbe80ea2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 3, 4, 5, 6, 7}\n"
     ]
    }
   ],
   "source": [
    "set4 = {1, 2, 3, 4, 5, 6, 7}\n",
    "set4.discard(2)\n",
    "print(set4)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5f712bea",
   "metadata": {},
   "source": [
    "### 5. Remove an Item if Present in the Set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "a9cedeeb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 5, 6, 7, 8, 9}\n"
     ]
    }
   ],
   "source": [
    "set5 = {1, 2, 3, 4, 5, 6, 7, 8, 9}\n",
    "set5.remove(4)\n",
    "print(set5)"
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
