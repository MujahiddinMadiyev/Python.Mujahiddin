{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2fe61781",
   "metadata": {},
   "source": [
    "# Homework"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "82cb1ad7",
   "metadata": {},
   "source": [
    "# Task"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e60e6bbd",
   "metadata": {},
   "source": [
    "# Problems"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c3412e6",
   "metadata": {},
   "source": [
    "### 1. is_prime(n) funksiyasi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18f98ec6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "def is_prime(n):\n",
    "    if n <= 1:\n",
    "        return False\n",
    "    for i in range(2, int(n**0.5)+1):\n",
    "        if n % i == 0:\n",
    "            return False\n",
    "    return True\n",
    "print(is_prime(4))\n",
    "print(is_prime(7))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8cb2b09d",
   "metadata": {},
   "source": [
    "### 2. digit_sum(k) funksiyasi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "68ded5bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "def digit_sum(k):\n",
    "    return sum(map(int, str(k)))\n",
    "print(digit_sum(24))\n",
    "print(digit_sum(502))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fcc797f3",
   "metadata": {},
   "source": [
    "### 3. Ikki sonning darajalari"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "1a95dead",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 4 8\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "def powers_of_two(N):\n",
    "    result = []\n",
    "    power = 1\n",
    "    while (value := 2 ** power) <= N:\n",
    "        result.append(value)\n",
    "        power += 1\n",
    "    print(*result)\n",
    "print(powers_of_two(10))\n"
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
