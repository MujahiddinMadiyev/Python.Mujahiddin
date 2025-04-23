{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8446fe14",
   "metadata": {},
   "source": [
    "# Homework:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8f6cff83",
   "metadata": {},
   "source": [
    "# Python Exception Handling: Exercises, Solutions, and Practice"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f26e20fa",
   "metadata": {},
   "source": [
    "## Exception Handling Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b6613a10",
   "metadata": {},
   "source": [
    "### 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d74752d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: Cannot divide by zero.\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    num = int(input(\"Enter a number to divide 10 by: \"))\n",
    "    result = 10 / num\n",
    "    print(\"Result:\", result)\n",
    "except ZeroDivisionError:\n",
    "    print(\"Error: Cannot divide by zero.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e566a3e8",
   "metadata": {},
   "source": [
    "### 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "136e91b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: That was not a valid integer.\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    num = int(input(\"Enter an integer: \"))\n",
    "    print(\"You entered:\", num)\n",
    "except ValueError:\n",
    "    print(\"Error: That was not a valid integer.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d2ee42db",
   "metadata": {},
   "source": [
    "### 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c1ee856a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: File not found.\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    file = open(\"non_existing_file.txt\", \"r\")\n",
    "except FileNotFoundError:\n",
    "    print(\"Error: File not found.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c8752b47",
   "metadata": {},
   "source": [
    "### 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "bf3729fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum is: 13.0\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    a = float(input(\"Enter first number: \"))\n",
    "    b = float(input(\"Enter second number: \"))\n",
    "    print(\"Sum is:\", a + b)\n",
    "except ValueError:\n",
    "    raise TypeError(\"Both inputs must be numbers.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5c96182d",
   "metadata": {},
   "source": [
    "### 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3899984d",
   "metadata": {},
   "outputs": [],
   "source": [
    "try:\n",
    "    file = open(\"/root/secret.txt\", \"r\")\n",
    "except PermissionError:\n",
    "    print(\"Error: You do not have permission to access this file.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9bf08d22",
   "metadata": {},
   "source": [
    "### 6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a6af1658",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: Index out of range.\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    my_list = [1, 2, 3]\n",
    "    print(my_list[5])\n",
    "except IndexError:\n",
    "    print(\"Error: Index out of range.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "46ba81f6",
   "metadata": {},
   "source": [
    "### 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "233a8706",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You entered: 9\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    num = input(\"Enter a number (Ctrl+C to cancel): \")\n",
    "    print(\"You entered:\", num)\n",
    "except KeyboardInterrupt:\n",
    "    print(\"\\nInput cancelled by user.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fe4fed80",
   "metadata": {},
   "source": [
    "### 8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "0e4ee3a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Arithmetic error occurred.\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    a = 10\n",
    "    b = 0\n",
    "    result = a / b\n",
    "except ArithmeticError:\n",
    "    print(\"Arithmetic error occurred.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7cde8ba9",
   "metadata": {},
   "source": [
    "### 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3026cb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "try:\n",
    "    with open(\"example.txt\", encoding=\"utf-8\") as f:\n",
    "        content = f.read()\n",
    "        print(content)\n",
    "except UnicodeDecodeError:\n",
    "    print(\"Error: Could not decode file due to encoding issue.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2fc162ba",
   "metadata": {},
   "source": [
    "### 10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "87a8b057",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: List object has no attribute 'upper'.\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    my_list = [1, 2, 3]\n",
    "    my_list.upper()\n",
    "except AttributeError:\n",
    "    print(\"Error: List object has no attribute 'upper'.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "318d708b",
   "metadata": {},
   "source": [
    "# Python File Input Output: Exercises, Practice, Solution"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "350a0272",
   "metadata": {},
   "source": [
    "## File Input/Output Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c7b83f24",
   "metadata": {},
   "source": [
    "### 1. Write a Python program to read an entire text file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70b26efd",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    print(f.read())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "09525b57",
   "metadata": {},
   "source": [
    "### 2. Write a Python program to read first n lines of a file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c2bb3853",
   "metadata": {},
   "outputs": [],
   "source": [
    "n = 3\n",
    "with open(\"example.txt\", \"r\") as f:\n",
    "    for i in range(n):\n",
    "        print(f.readline(), end=\"\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b150424",
   "metadata": {},
   "source": [
    "### 3. Write a Python program to append text to a file and display the text."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "548cd835",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"example.txt\", \"a\") as f:\n",
    "    f.write(\"\\nThis is an appended line.\")\n",
    "\n",
    "with open(\"example.txt\", \"r\") as f:\n",
    "    print(f.read())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "248bed6f",
   "metadata": {},
   "source": [
    "### 4. Write a Python program to read last n lines of a file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33ae7bca",
   "metadata": {},
   "outputs": [],
   "source": [
    "n = 2\n",
    "with open(\"example.txt\", \"r\") as f:\n",
    "    lines = f.readlines()\n",
    "    print(\"\".join(lines[-n:]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5189409f",
   "metadata": {},
   "source": [
    "### 5. Write a Python program to read a file line by line and store it into a list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1bc04df1",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    lines = f.readlines()\n",
    "print(lines)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17731aa8",
   "metadata": {},
   "source": [
    "### 6. Write a Python program to read a file line by line and store it into a variable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a356dcc",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    content = \"\"\n",
    "    for line in f:\n",
    "        content += line\n",
    "print(content)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d059df24",
   "metadata": {},
   "source": [
    "### 7. Write a Python program to read a file line by line and store it into an array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6247cd87",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    array = [line.strip() for line in f]\n",
    "print(array)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47e98635",
   "metadata": {},
   "source": [
    "### 8. Write a Python program to find the longest words."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca109191",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    words = f.read().split()\n",
    "    longest = max(words, key=len)\n",
    "print(\"Longest word:\", longest)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "34e6df09",
   "metadata": {},
   "source": [
    "### 9. Write a Python program to count the number of lines in a text file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c2e807b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    print(\"Number of lines:\", len(f.readlines()))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "739fc74e",
   "metadata": {},
   "source": [
    "### 10. Write a Python program to count the frequency of words in a file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fe120606",
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import Counter\n",
    "\n",
    "with open(\"example.txt\", \"r\") as f:\n",
    "    words = f.read().split()\n",
    "    word_freq = Counter(words)\n",
    "print(word_freq)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c95d58da",
   "metadata": {},
   "source": [
    "### 11. Write a Python program to get the file size of a plain file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7058a88",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "print(\"File size:\", os.path.getsize(\"example.txt\"), \"bytes\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc9e1c98",
   "metadata": {},
   "source": [
    "### 12. Write a Python program to write a list to a file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a16a169e",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_list = [\"Python\", \"Java\", \"C++\"]\n",
    "with open(\"languages.txt\", \"w\") as f:\n",
    "    for item in my_list:\n",
    "        f.write(item + \"\\n\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2692992e",
   "metadata": {},
   "source": [
    "### 13. Write a Python program to copy the contents of a file to another file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7249f6e",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"example.txt\", \"r\") as src, open(\"copy.txt\", \"w\") as dest:\n",
    "    dest.write(src.read())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "34fb9abc",
   "metadata": {},
   "source": [
    "### 14. Write a Python program to combine each line from the first file with the corresponding line in the second file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "236d0ea2",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"file1.txt\", \"r\") as f1, open(\"file2.txt\", \"r\") as f2:\n",
    "    for line1, line2 in zip(f1, f2):\n",
    "        print(line1.strip() + \" \" + line2.strip())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb87cfb7",
   "metadata": {},
   "source": [
    "### 15. Write a Python program to read a random line from a file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74ba6fd1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "with open(\"example.txt\", \"r\") as f:\n",
    "    lines = f.readlines()\n",
    "    print(random.choice(lines))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b69c301a",
   "metadata": {},
   "source": [
    "### 16. Write a Python program to assess if a file is closed or not."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18ec5d4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "f = open(\"example.txt\", \"r\")\n",
    "print(\"Is file closed?\", f.closed)\n",
    "f.close()\n",
    "print(\"Is file closed?\", f.closed)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3cd7cbf5",
   "metadata": {},
   "source": [
    "### 17. Write a Python program to remove newline characters from a file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "419ded3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    lines = f.read().splitlines()\n",
    "print(lines)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7cb6f988",
   "metadata": {},
   "source": [
    "### 18. Write a Python program that takes a text file as input and returns the number of words in a given text file.\n",
    "\n",
    "(Note: Some words can be separated by a comma with no space.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49a9de6a",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"example.txt\", \"r\") as f:\n",
    "    text = f.read().replace(\",\", \" \")\n",
    "    word_count = len(text.split())\n",
    "print(\"Word count:\", word_count)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a55c9304",
   "metadata": {},
   "source": [
    "### 19. Write a Python program to extract characters from various text files and put them into a list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18cca2d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "chars = []\n",
    "for filename in os.listdir(\"text_files\"):\n",
    "    if filename.endswith(\".txt\"):\n",
    "        with open(os.path.join(\"text_files\", filename), \"r\") as f:\n",
    "            chars.extend(list(f.read()))\n",
    "print(chars)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "87e3dd51",
   "metadata": {},
   "source": [
    "### 20. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a26bf60",
   "metadata": {},
   "outputs": [],
   "source": [
    "import string\n",
    "\n",
    "for letter in string.ascii_uppercase:\n",
    "    with open(f\"{letter}.txt\", \"w\") as f:\n",
    "        f.write(f\"This is file {letter}.txt\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "95bc78ad",
   "metadata": {},
   "source": [
    "### 21. Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9300cb7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import string\n",
    "\n",
    "letters_per_line = 5\n",
    "alphabet = string.ascii_uppercase\n",
    "\n",
    "with open(\"alphabet.txt\", \"w\") as f:\n",
    "    for i in range(0, len(alphabet), letters_per_line):\n",
    "        f.write(\"\".join(alphabet[i:i+letters_per_line]) + \"\\n\")"
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
