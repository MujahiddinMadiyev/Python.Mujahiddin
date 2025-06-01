{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bf0d0d8c",
   "metadata": {},
   "source": [
    "# 1. Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6aab4b02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You are 25 years, 8 months, and 27 days old.\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime, date\n",
    "from dateutil.relativedelta import relativedelta\n",
    "\n",
    "def calculate_age_from_input():\n",
    "    birthdate_str = input(\"Enter your birthdate (YYYY-MM-DD): \")\n",
    "    \n",
    "    birthdate = datetime.strptime(birthdate_str, \"%Y-%m-%d\").date()\n",
    "    today = date.today()\n",
    "\n",
    "    age_diff = relativedelta(today, birthdate)\n",
    "\n",
    "    print(f\"You are {age_diff.years} years, {age_diff.months} months, and {age_diff.days} days old.\")\n",
    "\n",
    "calculate_age_from_input()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6fcc9f5f",
   "metadata": {},
   "source": [
    "# 2. Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3b78bb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your next birthday is in 95 days.\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime, date, timedelta\n",
    "\n",
    "def days_until_next_birthday():\n",
    "    birthdate_str = input(\"Enter your birthdate (YYYY-MM-DD): \")\n",
    "    \n",
    "\n",
    "    birthdate = datetime.strptime(birthdate_str, \"%Y-%m-%d\").date()\n",
    "    today = date.today()\n",
    "\n",
    "    next_birthday = birthdate.replace(year=today.year)\n",
    "\n",
    "    if next_birthday < today:\n",
    "            next_birthday = next_birthday.replace(year=today.year + 1)\n",
    "\n",
    "    days_left = (next_birthday - today).days\n",
    "\n",
    "    print(f\"Your next birthday is in {days_left} days.\")\n",
    "\n",
    "days_until_next_birthday()   "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a71de0d2",
   "metadata": {},
   "source": [
    "# 3. Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0059fa74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The meeting will end at: 2025-05-18 20:00\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime, timedelta\n",
    "\n",
    "def meeting_scheduler():\n",
    "\n",
    "    current_str = input(\"Enter the current date and time (YYYY-MM-DD HH:MM): \")\n",
    "    current_dt = datetime.strptime(current_str, \"%Y-%m-%d %H:%M\")\n",
    "\n",
    "    hours = int(input(\"Enter meeting duration - hours: \"))\n",
    "    minutes = int(input(\"Enter meeting duration - minutes: \"))\n",
    "\n",
    "    duration = timedelta(hours=hours, minutes=minutes)\n",
    "    end_dt = current_dt + duration\n",
    "\n",
    "    print(f\"The meeting will end at: {end_dt.strftime('%Y-%m-%d %H:%M')}\")\n",
    "\n",
    "meeting_scheduler()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6b7b0428",
   "metadata": {},
   "source": [
    "# 4. Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b0361e57",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Timezone Converter ---\n",
      "Converted datetime: 2025-05-19 06:00 JST+0900\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime\n",
    "import pytz\n",
    "\n",
    "print(\"\\n--- Timezone Converter ---\")\n",
    "date_str = input(\"Enter date and time (YYYY-MM-DD HH:MM): \")\n",
    "from_tz_str = input(\"Enter your current timezone (e.g., 'US/Eastern'): \")\n",
    "to_tz_str = input(\"Enter the target timezone (e.g., 'Asia/Tokyo'): \")\n",
    "\n",
    "dt = datetime.strptime(date_str, \"%Y-%m-%d %H:%M\")\n",
    "from_tz = pytz.timezone(from_tz_str)\n",
    "to_tz = pytz.timezone(to_tz_str)\n",
    "\n",
    "local_dt = from_tz.localize(dt)\n",
    "target_dt = local_dt.astimezone(to_tz)\n",
    "\n",
    "print(\"Converted datetime:\", target_dt.strftime(\"%Y-%m-%d %H:%M %Z%z\"))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b56ced6",
   "metadata": {},
   "source": []
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
