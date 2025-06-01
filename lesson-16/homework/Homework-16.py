{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f21d008e",
   "metadata": {},
   "source": [
    "# 1. 1. Convert List to 1D Array\n",
    "Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.\n",
    "\n",
    "Expected Output:\n",
    "\n",
    "Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d29ce1af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original List: [12.23, 13.32, 100, 36.32]\n",
      "One-dimensional NumPy array: [ 12.23  13.32 100.    36.32]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "lst = [12.23, 13.32, 100, 36.32]\n",
    "arr = np.array(lst)\n",
    "print(\"Original List:\", lst)\n",
    "print(\"One-dimensional NumPy array:\", arr)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e76ad6c1",
   "metadata": {},
   "source": [
    "# 2. Create 3x3 Matrix (2?10)\n",
    "Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.\n",
    "\n",
    "Expected Output:\n",
    "\n",
    "[[ 2 3 4] [ 5 6 7] [ 8 9 10]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "802d05a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 2  3  4]\n",
      " [ 5  6  7]\n",
      " [ 8  9 10]]\n"
     ]
    }
   ],
   "source": [
    "arr = np.arange(2, 11).reshape(3, 3)\n",
    "print(arr)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e9b76078",
   "metadata": {},
   "source": [
    "# 3. Null Vector (10) & Update Sixth Value\n",
    "Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.\n",
    "\n",
    "[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]\n",
    "\n",
    "Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e0c8ebd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original null vector: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]\n",
      "Updated vector: [ 0.  0.  0.  0.  0.  0. 11.  0.  0.  0.]\n"
     ]
    }
   ],
   "source": [
    "vector = np.zeros(10)\n",
    "print(\"Original null vector:\", vector)\n",
    "\n",
    "vector[6] = 11\n",
    "print(\"Updated vector:\", vector)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "62181c17",
   "metadata": {},
   "source": [
    "# 4. Array from 12 to 38\n",
    "Write a NumPy program to create an array with values ranging from 12 to 38.\n",
    "\n",
    "Expected Output:\n",
    "\n",
    "[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "434f466d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35\n",
      " 36 37]\n"
     ]
    }
   ],
   "source": [
    "arr = np.arange(12, 38)\n",
    "print(arr)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d58e1a7",
   "metadata": {},
   "source": [
    "# 5. Convert Array to Float Type\n",
    "Write a NumPy program to convert an array to a floating type.\n",
    "\n",
    "Sample output:\n",
    "\n",
    "Original array [1, 2, 3, 4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1725d14f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original array: [1 2 3 4]\n",
      "Float array: [1. 2. 3. 4.]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([1, 2, 3, 4])\n",
    "float_arr = arr.astype(float)\n",
    "print(\"Original array:\", arr)\n",
    "print(\"Float array:\", float_arr)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eb6c2658",
   "metadata": {},
   "source": [
    "# 6. Celsius to Fahrenheit Conversion\n",
    "Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.\n",
    "\n",
    "Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]\n",
    "\n",
    "Expected Output:\n",
    "\n",
    "Values in Fahrenheit degrees: [ 0. 12. 45.21 34. 99.91 32. ]\n",
    "\n",
    "Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]\n",
    "\n",
    "Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]\n",
    "\n",
    "Values in Fahrenheit degrees: [-0. 12. 45.21 34. 99.91 32. ]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5e05aa06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Values in Centigrade degrees: [-17.78 -11.11   7.34   1.11  37.73   0.  ]\n",
      "Values in Fahrenheit degrees: [-4.0000e-03  1.2002e+01  4.5212e+01  3.3998e+01  9.9914e+01  3.2000e+01]\n"
     ]
    }
   ],
   "source": [
    "celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])\n",
    "fahrenheit = (celsius * 9/5) + 32\n",
    "\n",
    "print(\"Values in Centigrade degrees:\", celsius)\n",
    "print(\"Values in Fahrenheit degrees:\", fahrenheit)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2691fba0",
   "metadata": {},
   "source": [
    "# 7. Append Values to Array (Do self-tudy)\n",
    "Write a NumPy program to append values to the end of an array.\n",
    "\n",
    "Expected Output:\n",
    "\n",
    "Original array: [10, 20, 30]\n",
    "\n",
    "After append values to the end of the array: [10 20 30 40 50 60 70 80 90]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "cca3d850",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original array: [10 20 30]\n",
      "After append: [10 20 30 40 50 60 70 80 90]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([10, 20, 30])\n",
    "appended = np.append(arr, [40, 50, 60, 70, 80, 90])\n",
    "print(\"Original array:\", arr)\n",
    "print(\"After append:\", appended)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd0ad280",
   "metadata": {},
   "source": [
    "# 8. Array Statistical Functions (Do self-tudy)\n",
    "Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "40b92009",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Minimum value: 0.002534168297961492\n",
      "Maximum value: 0.9983405846778121\n"
     ]
    }
   ],
   "source": [
    "arr = np.random.rand(10, 10)\n",
    "print(\"Minimum value:\", np.min(arr))\n",
    "print(\"Maximum value:\", np.max(arr))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f77bb93e",
   "metadata": {},
   "source": [
    "# 9 Find min and max\n",
    "Create a 10x10 array with random values and find the minimum and maximum values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "06ea8591",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Minimum value: 0.011480647964580482\n",
      "Maximum value: 0.9965555200721425\n"
     ]
    }
   ],
   "source": [
    "arr = np.random.rand(10, 10)\n",
    "print(\"Minimum value:\", np.min(arr))\n",
    "print(\"Maximum value:\", np.max(arr))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e937ed1c",
   "metadata": {},
   "source": [
    "# 10\n",
    "Create a 3x3x3 array with random values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d9109b4e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[0.24752103 0.75938108 0.41301316]\n",
      "  [0.06375976 0.492624   0.7358587 ]\n",
      "  [0.51986774 0.04196695 0.15610131]]\n",
      "\n",
      " [[0.97565026 0.0112501  0.71343255]\n",
      "  [0.96976272 0.3482092  0.77452588]\n",
      "  [0.8432788  0.89741029 0.20748994]]\n",
      "\n",
      " [[0.43101584 0.34019654 0.22087132]\n",
      "  [0.66492237 0.01793164 0.67866019]\n",
      "  [0.0219558  0.29504894 0.70091439]]]\n"
     ]
    }
   ],
   "source": [
    "arr = np.random.rand(3, 3, 3)\n",
    "print(arr)\n"
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
