{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4d99f4e4",
   "metadata": {},
   "source": [
    "# Homework 1:\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} df = pd.DataFrame(data)\n",
    "\n",
    "1. Rename column names using function. \"First Name\" --> \"first_name\", \"Age\" --> \"age\n",
    "2. Print the first 3 rows of the DataFrame\n",
    "3. Find the mean age of the individuals\n",
    "4. Select and print only the 'Name' and 'City' columns\n",
    "5. Add a new column 'Salary' with random salary values\n",
    "6. Display summary statistics of the DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "43605d0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First 3 rows:\n",
      "   first_name  age           City\n",
      "0      Alice   25       New York\n",
      "1        Bob   30  San Francisco\n",
      "2    Charlie   35    Los Angeles\n",
      "\n",
      "Mean age: 32.5\n",
      "\n",
      "Name and City columns:\n",
      "   first_name           City\n",
      "0      Alice       New York\n",
      "1        Bob  San Francisco\n",
      "2    Charlie    Los Angeles\n",
      "3      David        Chicago\n",
      "\n",
      "With Salary column:\n",
      "   first_name  age           City  Salary\n",
      "0      Alice   25       New York   62096\n",
      "1        Bob   30  San Francisco   50500\n",
      "2    Charlie   35    Los Angeles   63947\n",
      "3      David   40        Chicago   85195\n",
      "\n",
      "Summary Statistics:\n",
      "              age        Salary\n",
      "count   4.000000      4.000000\n",
      "mean   32.500000  65434.500000\n",
      "std     6.454972  14455.389871\n",
      "min    25.000000  50500.000000\n",
      "25%    28.750000  59197.000000\n",
      "50%    32.500000  63021.500000\n",
      "75%    36.250000  69259.000000\n",
      "max    40.000000  85195.000000\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# Original data\n",
    "data = {\n",
    "    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],\n",
    "    'Age': [25, 30, 35, 40],\n",
    "    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']\n",
    "}\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "# 1. Rename columns\n",
    "df = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})\n",
    "\n",
    "# 2. Print the first 3 rows\n",
    "print(\"First 3 rows:\\n\", df.head(3))\n",
    "\n",
    "# 3. Mean age\n",
    "print(\"\\nMean age:\", df['age'].mean())\n",
    "\n",
    "# 4. Select and print only 'first_name' and 'City'\n",
    "print(\"\\nName and City columns:\\n\", df[['first_name', 'City']])\n",
    "\n",
    "# 5. Add a new 'Salary' column with random values\n",
    "df['Salary'] = np.random.randint(50000, 100000, size=len(df))\n",
    "print(\"\\nWith Salary column:\\n\", df)\n",
    "\n",
    "# 6. Summary statistics\n",
    "print(\"\\nSummary Statistics:\\n\", df.describe())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "589669ad",
   "metadata": {},
   "source": [
    "# Homework 2:\n",
    "\n",
    "1. Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.\n",
    "\n",
    "Month\tSales\tExpenses\n",
    "\n",
    "Jan\t5000\t3000\n",
    "\n",
    "Feb\t6000\t3500\n",
    "\n",
    "Mar\t7500\t4000\n",
    "\n",
    "Apr\t8000\t4500\n",
    "\n",
    "2. Calculate and display the maximum sales and expenses.\n",
    "3. Calculate and display the minimum sales and expenses.\n",
    "4. Calculate and display the average sales and expenses."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1b46c5ae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Max Sales: 8000\n",
      "Max Expenses: 4500\n",
      "Min Sales: 5000\n",
      "Min Expenses: 3000\n",
      "Avg Sales: 6625.0\n",
      "Avg Expenses: 3750.0\n"
     ]
    }
   ],
   "source": [
    "# Create DataFrame\n",
    "sales_data = {\n",
    "    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],\n",
    "    'Sales': [5000, 6000, 7500, 8000],\n",
    "    'Expenses': [3000, 3500, 4000, 4500]\n",
    "}\n",
    "df2 = pd.DataFrame(sales_data)\n",
    "\n",
    "# 2. Max sales and expenses\n",
    "print(\"Max Sales:\", df2['Sales'].max())\n",
    "print(\"Max Expenses:\", df2['Expenses'].max())\n",
    "\n",
    "# 3. Min sales and expenses\n",
    "print(\"Min Sales:\", df2['Sales'].min())\n",
    "print(\"Min Expenses:\", df2['Expenses'].min())\n",
    "\n",
    "# 4. Average sales and expenses\n",
    "print(\"Avg Sales:\", df2['Sales'].mean())\n",
    "print(\"Avg Expenses:\", df2['Expenses'].mean())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e867df5e",
   "metadata": {},
   "source": [
    "# Homework 3:\n",
    "\n",
    "1. Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.\n",
    "\n",
    "Category\tJanuary\tFebruary\tMarch\tApril\n",
    "\n",
    "Rent\t1200\t1300\t1400\t1500\n",
    "\n",
    "Utilities\t200\t220\t240\t250\n",
    "\n",
    "Groceries\t300\t320\t330\t350\n",
    "\n",
    "Entertainment\t150\t160\t170\t180\n",
    "\n",
    "2. Calculate and display the maximum expense for each category.\n",
    "3. Calculate and display the minimum expense for each category.\n",
    "4. Calculate and display the average expense for each category.\n",
    "\n",
    "In this task, use .set_index method to make Category column as index.\n",
    "\n",
    "Try this code, learn it and use it in the task.\n",
    "\n",
    "expenses.set_index('Category')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1dc12284",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Max expense per category:\n",
      " Category\n",
      "Rent             1500\n",
      "Utilities         250\n",
      "Groceries         350\n",
      "Entertainment     180\n",
      "dtype: int64\n",
      "\n",
      "Min expense per category:\n",
      " Category\n",
      "Rent             1200\n",
      "Utilities         200\n",
      "Groceries         300\n",
      "Entertainment     150\n",
      "dtype: int64\n",
      "\n",
      "Average expense per category:\n",
      " Category\n",
      "Rent             1350.0\n",
      "Utilities         227.5\n",
      "Groceries         325.0\n",
      "Entertainment     165.0\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Create DataFrame\n",
    "expense_data = {\n",
    "    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],\n",
    "    'January': [1200, 200, 300, 150],\n",
    "    'February': [1300, 220, 320, 160],\n",
    "    'March': [1400, 240, 330, 170],\n",
    "    'April': [1500, 250, 350, 180]\n",
    "}\n",
    "expenses = pd.DataFrame(expense_data)\n",
    "\n",
    "# Set index to Category\n",
    "expenses = expenses.set_index('Category')\n",
    "\n",
    "# 2. Max per category\n",
    "print(\"\\nMax expense per category:\\n\", expenses.max(axis=1))\n",
    "\n",
    "# 3. Min per category\n",
    "print(\"\\nMin expense per category:\\n\", expenses.min(axis=1))\n",
    "\n",
    "# 4. Average per category\n",
    "print(\"\\nAverage expense per category:\\n\", expenses.mean(axis=1))\n"
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
