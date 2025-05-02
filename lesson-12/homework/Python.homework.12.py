{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c7aa550c",
   "metadata": {},
   "source": [
    "# Homework:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "48eac4b2",
   "metadata": {},
   "source": [
    "## Exercise 1: Threaded Prime Number Checker"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cdf03cec",
   "metadata": {},
   "outputs": [],
   "source": [
    "import threading\n",
    "\n",
    "def is_prime(n):\n",
    "    if n < 2:\n",
    "        return False\n",
    "    for i in range(2, int(n**0.5) + 1):\n",
    "        if n % i == 0:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def check_primes_in_range(start, end, result):\n",
    "    primes = []\n",
    "    for num in range(start, end):\n",
    "        if is_prime(num):\n",
    "            primes.append(num)\n",
    "    result.extend(primes)\n",
    "\n",
    "def threaded_prime_checker(start, end, num_threads=4):\n",
    "    threads = []\n",
    "    result = []\n",
    "    results_lock = threading.Lock()\n",
    "    step = (end - start) // num_threads\n",
    "\n",
    "    def worker(s, e):\n",
    "        local_result = []\n",
    "        check_primes_in_range(s, e, local_result)\n",
    "        with results_lock:\n",
    "            result.extend(local_result)\n",
    "\n",
    "    for i in range(num_threads):\n",
    "        s = start + i * step\n",
    "        e = start + (i + 1) * step if i < num_threads - 1 else end\n",
    "        thread = threading.Thread(target=worker, args=(s, e))\n",
    "        threads.append(thread)\n",
    "        thread.start()\n",
    "\n",
    "    for thread in threads:\n",
    "        thread.join()\n",
    "\n",
    "    print(f\"Primes between {start} and {end}: {sorted(result)}\")\n",
    "\n",
    "# Example usage\n",
    "# threaded_prime_checker(1, 100, 4)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "320df568",
   "metadata": {},
   "source": [
    "## Exercise 2: Threaded File Processing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "da786a44",
   "metadata": {},
   "outputs": [],
   "source": [
    "import threading\n",
    "from collections import defaultdict\n",
    "\n",
    "def count_words(lines, word_count, lock):\n",
    "    local_count = defaultdict(int)\n",
    "    for line in lines:\n",
    "        for word in line.strip().split():\n",
    "            word = word.lower().strip('.,!?')\n",
    "            local_count[word] += 1\n",
    "    with lock:\n",
    "        for word, count in local_count.items():\n",
    "            word_count[word] += count\n",
    "\n",
    "def threaded_file_word_count(file_path, num_threads=4):\n",
    "    with open(file_path, 'r') as file:\n",
    "        lines = file.readlines()\n",
    "\n",
    "    threads = []\n",
    "    word_count = defaultdict(int)\n",
    "    lock = threading.Lock()\n",
    "    step = len(lines) // num_threads\n",
    "\n",
    "    for i in range(num_threads):\n",
    "        start = i * step\n",
    "        end = (i + 1) * step if i < num_threads - 1 else len(lines)\n",
    "        thread = threading.Thread(target=count_words, args=(lines[start:end], word_count, lock))\n",
    "        threads.append(thread)\n",
    "        thread.start()\n",
    "\n",
    "    for thread in threads:\n",
    "        thread.join()\n",
    "\n",
    "    print(\"Word Occurrences:\")\n",
    "    for word, count in sorted(word_count.items()):\n",
    "        print(f\"{word}: {count}\")\n",
    "\n",
    "# Example usage:\n",
    "# threaded_file_word_count(\"large_text_file.txt\", 4)\n"
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
