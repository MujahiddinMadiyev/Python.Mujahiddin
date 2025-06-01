{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b6f0b034",
   "metadata": {},
   "source": [
    "# 1. Task: JSON Parsing\n",
    "write a Python script that reads the students.jon JSON file and prints details of each student."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9935703",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "\n",
    "print(\"\\n--- JSON Parsing: Students ---\")\n",
    "with open(\"students.json\", \"r\") as file:\n",
    "    data = json.load(file)\n",
    "\n",
    "for student in data.get(\"students\", []):\n",
    "    print(f\"Name: {student['name']}\")\n",
    "    print(f\"Age: {student['age']}\")\n",
    "    print(f\"Grade: {student['grade']}\")\n",
    "    print(\"-\" * 20)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cbe95520",
   "metadata": {},
   "source": [
    "# 2. Task: Weather API\n",
    "Use this url : https://openweathermap.org/\n",
    "Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6bd4d03b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Weather Info: Tashkent ---\n",
      "Error fetching weather data: Invalid API key. Please see https://openweathermap.org/faq#error401 for more info.\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "API_KEY = \"YOUR_API_KEY\"\n",
    "CITY = \"Tashkent\"\n",
    "URL = f\"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric\"\n",
    "\n",
    "print(\"\\n--- Weather Info: Tashkent ---\")\n",
    "response = requests.get(URL)\n",
    "weather = response.json()\n",
    "\n",
    "if weather.get(\"cod\") == 200:\n",
    "    main = weather[\"main\"]\n",
    "    print(\"Temperature:\", main[\"temp\"], \"°C\")\n",
    "    print(\"Humidity:\", main[\"humidity\"], \"%\")\n",
    "    print(\"Weather:\", weather[\"weather\"][0][\"description\"])\n",
    "else:\n",
    "    print(\"Error fetching weather data:\", weather.get(\"message\"))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c3c80f1b",
   "metadata": {},
   "source": [
    "# 3. Task: JSON Modification\n",
    "Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c3bb30e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "\n",
    "def load_books():\n",
    "    with open(\"books.json\", \"r\") as file:\n",
    "        return json.load(file)\n",
    "\n",
    "def save_books(books):\n",
    "    with open(\"books.json\", \"w\") as file:\n",
    "        json.dump(books, file, indent=4)\n",
    "\n",
    "def add_book():\n",
    "    title = input(\"Title: \")\n",
    "    author = input(\"Author: \")\n",
    "    books.append({\"title\": title, \"author\": author})\n",
    "    save_books(books)\n",
    "\n",
    "def update_book():\n",
    "    title = input(\"Enter book title to update: \")\n",
    "    for book in books:\n",
    "        if book[\"title\"] == title:\n",
    "            book[\"title\"] = input(\"New title: \")\n",
    "            book[\"author\"] = input(\"New author: \")\n",
    "            save_books(books)\n",
    "            return\n",
    "    print(\"Book not found.\")\n",
    "\n",
    "def delete_book():\n",
    "    title = input(\"Enter book title to delete: \")\n",
    "    global books\n",
    "    books = [book for book in books if book[\"title\"] != title]\n",
    "    save_books(books)\n",
    "\n",
    "books = load_books()\n",
    "\n",
    "while True:\n",
    "    print(\"\\n1. Add Book\\n2. Update Book\\n3. Delete Book\\n4. View Books\\n5. Exit\")\n",
    "    choice = input(\"Choice: \")\n",
    "    if choice == \"1\":\n",
    "        add_book()\n",
    "    elif choice == \"2\":\n",
    "        update_book()\n",
    "    elif choice == \"3\":\n",
    "        delete_book()\n",
    "    elif choice == \"4\":\n",
    "        for b in books:\n",
    "            print(f\"{b['title']} by {b['author']}\")\n",
    "    elif choice == \"5\":\n",
    "        break\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8f03e03b",
   "metadata": {},
   "source": [
    "# 4. Task: Movie Recommendation System\n",
    "Use this url http://www.omdbapi.com/ to fetch information about movies.\n",
    "Create a program that asks users for a movie genre and recommends a random movie from that genre."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "36b236c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Movie not found.\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import random\n",
    "\n",
    "API_KEY = \"YOUR_OMDB_API_KEY\"\n",
    "GENRE = input(\"Enter a movie genre (e.g. Action, Comedy): \")\n",
    "\n",
    "# Sample titles by genre (in a real app, you'd use a DB or larger dataset)\n",
    "genre_movies = {\n",
    "    \"Action\": [\"Mad Max: Fury Road\", \"John Wick\", \"Die Hard\"],\n",
    "    \"Comedy\": [\"Superbad\", \"The Mask\", \"Step Brothers\"],\n",
    "    \"Drama\": [\"Forrest Gump\", \"The Shawshank Redemption\", \"Fight Club\"]\n",
    "}\n",
    "\n",
    "movies = genre_movies.get(GENRE.title())\n",
    "if not movies:\n",
    "    print(\"No movies available for that genre.\")\n",
    "else:\n",
    "    movie = random.choice(movies)\n",
    "    URL = f\"http://www.omdbapi.com/?t={movie}&apikey={API_KEY}\"\n",
    "\n",
    "    response = requests.get(URL)\n",
    "    data = response.json()\n",
    "\n",
    "    if data.get(\"Response\") == \"True\":\n",
    "        print(f\"\\n--- Movie Recommendation ---\")\n",
    "        print(\"Title:\", data[\"Title\"])\n",
    "        print(\"Year:\", data[\"Year\"])\n",
    "        print(\"Genre:\", data[\"Genre\"])\n",
    "        print(\"Plot:\", data[\"Plot\"])\n",
    "        print(\"IMDB Rating:\", data[\"imdbRating\"])\n",
    "    else:\n",
    "        print(\"Movie not found.\")\n"
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
