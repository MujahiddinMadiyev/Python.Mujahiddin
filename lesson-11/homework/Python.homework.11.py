{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "002c4409",
   "metadata": {},
   "source": [
    "# Homework:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c9a0fbd9",
   "metadata": {},
   "source": [
    "## Create custom modules."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3e0ad2a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# math_operations.py\n",
    "\n",
    "def add(a, b):\n",
    "    return a + b\n",
    "\n",
    "def subtract(a, b):\n",
    "    return a - b\n",
    "\n",
    "def multiply(a, b):\n",
    "    return a * b\n",
    "\n",
    "def divide(a, b):\n",
    "    return a / b if b != 0 else \"Cannot divide by zero\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6c0f3820",
   "metadata": {},
   "outputs": [],
   "source": [
    "# string_utils.py\n",
    "\n",
    "def reverse_string(s):\n",
    "    return s[::-1]\n",
    "\n",
    "def count_vowels(s):\n",
    "    return sum(1 for char in s.lower() if char in 'aeiou')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ab6eb27f",
   "metadata": {},
   "source": [
    "## Create custom packages."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18d1bea7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# geometry/\n",
    "#     __init__.py\n",
    "#     circle.py\n",
    "\n",
    "# geometry/circle.py\n",
    "\n",
    "import math\n",
    "\n",
    "def calculate_area(radius):\n",
    "    return math.pi * radius ** 2\n",
    "\n",
    "def calculate_circumference(radius):\n",
    "    return 2 * math.pi * radius\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a1879281",
   "metadata": {},
   "outputs": [],
   "source": [
    "# file_operations/\n",
    "#    __init__.py\n",
    "#     file_reader.py\n",
    "#     file_writer.py\n",
    "\n",
    "# file_operations/file_reader.py\n",
    "\n",
    "def read_file(file_path):\n",
    "    with open(file_path, 'r') as file:\n",
    "        return file.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "29e4813a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# file_operations/file_writer.py\n",
    "\n",
    "def write_file(file_path, content):\n",
    "    with open(file_path, 'w') as file:\n",
    "        file.write(content)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "757bb039",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'math_operations'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[6]\u001b[39m\u001b[32m, line 4\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;66;03m# main.py\u001b[39;00m\n\u001b[32m      2\u001b[39m \n\u001b[32m      3\u001b[39m \u001b[38;5;66;03m# Using custom modules\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m4\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mmath_operations\u001b[39;00m\n\u001b[32m      5\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstring_utils\u001b[39;00m\n\u001b[32m      7\u001b[39m \u001b[38;5;66;03m# Using packages\u001b[39;00m\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'math_operations'"
     ]
    }
   ],
   "source": [
    "# main.py\n",
    "\n",
    "# Using custom modules\n",
    "import math_operations\n",
    "import string_utils\n",
    "\n",
    "# Using packages\n",
    "from geometry import circle\n",
    "from file_operations import file_reader, file_writer\n",
    "\n",
    "# Test math operations\n",
    "print(math_operations.add(5, 3))\n",
    "print(math_operations.divide(10, 2))\n",
    "\n",
    "# Test string utils\n",
    "print(string_utils.reverse_string(\"hello\"))\n",
    "print(string_utils.count_vowels(\"education\"))\n",
    "\n",
    "# Test geometry\n",
    "print(circle.calculate_area(7))\n",
    "print(circle.calculate_circumference(7))\n",
    "\n",
    "# Test file operations\n",
    "file_writer.write_file(\"example.txt\", \"Hello, World!\")\n",
    "print(file_reader.read_file(\"example.txt\"))\n"
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
