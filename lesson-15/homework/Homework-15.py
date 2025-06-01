{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "cd99303d",
   "metadata": {},
   "source": [
    "# 1. Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7813672f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x132c557bbc0>"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import sqlite3\n",
    "\n",
    "conn = sqlite3.connect(\"starfleet.db\")\n",
    "cur = conn.cursor()\n",
    "\n",
    "cur.execute(\"\"\"\n",
    "CREATE TABLE IF NOT EXISTS Roster (\n",
    "    Name TEXT,\n",
    "    Species TEXT,\n",
    "    Age INTEGER\n",
    ")\n",
    "\"\"\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "67ab68fa",
   "metadata": {},
   "source": [
    "# 2. Populate your new table with the following values:\n",
    "\n",
    "Name____________Species________Age\n",
    "\n",
    "Benjamin Sisko__Human_________40\n",
    "\n",
    "Jadzia Dax_______Trill_____________300\n",
    "\n",
    "Kira Nerys_______Bajoran_________29"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1c0faec3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x132c557bbc0>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cur.execute(\"DELETE FROM Roster\")  # Clear any existing data\n",
    "students = [\n",
    "    (\"Benjamin Sisko\", \"Human\", 40),\n",
    "    (\"Jadzia Dax\", \"Trill\", 300),\n",
    "    (\"Kira Nerys\", \"Bajoran\", 29)\n",
    "]\n",
    "cur.executemany(\"INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)\", students)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2c7522dd",
   "metadata": {},
   "source": [
    "# 3. Update the Name of Jadzia Dax to be Ezri Dax"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "91ea1031",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x132c557bbc0>"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cur.execute(\"\"\"\n",
    "UPDATE Roster\n",
    "SET Name = 'Ezri Dax'\n",
    "WHERE Name = 'Jadzia Dax'\n",
    "\"\"\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8ec49179",
   "metadata": {},
   "source": [
    "# 4. Display the Name and Age of everyone in the table classified as Bajoran."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "640519a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Bajoran Members ---\n",
      "Name: Kira Nerys, Age: 29\n"
     ]
    }
   ],
   "source": [
    "print(\"\\n--- Bajoran Members ---\")\n",
    "cur.execute(\"SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'\")\n",
    "for row in cur.fetchall():\n",
    "    print(f\"Name: {row[0]}, Age: {row[1]}\")\n",
    "\n",
    "conn.commit()\n",
    "conn.close()"
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
