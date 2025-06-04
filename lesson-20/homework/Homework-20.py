{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "9e3fb131",
   "metadata": {},
   "source": [
    "# Using chinook.db write pandas code."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e2d0edd",
   "metadata": {},
   "source": [
    "# 1. Customer Purchases Analysis:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc890df2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "import pandas as pd\n",
    "\n",
    "# Connect to the database\n",
    "conn = sqlite3.connect(\"chinook.db\")\n",
    "\n",
    "# Load customer and invoice data\n",
    "query = \"\"\"\n",
    "SELECT c.CustomerId, c.FirstName || ' ' || c.LastName AS CustomerName, \n",
    "       SUM(i.Total) AS TotalSpent\n",
    "FROM Customer c\n",
    "JOIN Invoice i ON c.CustomerId = i.CustomerId\n",
    "GROUP BY c.CustomerId\n",
    "ORDER BY TotalSpent DESC\n",
    "LIMIT 5;\n",
    "\"\"\"\n",
    "\n",
    "# Read data into a Pandas DataFrame\n",
    "top_customers = pd.read_sql_query(query, conn)\n",
    "\n",
    "# Display results\n",
    "print(top_customers)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c090b150",
   "metadata": {},
   "source": [
    "# 2. Album vs. Individual Track Purchases:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "005d5cde",
   "metadata": {},
   "outputs": [],
   "source": [
    "query = \"\"\"\n",
    "WITH AlbumPurchases AS (\n",
    "    SELECT il.InvoiceId, t.AlbumId, COUNT(DISTINCT il.TrackId) AS TracksPurchased,\n",
    "           (SELECT COUNT(*) FROM Track WHERE AlbumId = t.AlbumId) AS TotalTracksInAlbum\n",
    "    FROM InvoiceLine il\n",
    "    JOIN Track t ON il.TrackId = t.TrackId\n",
    "    GROUP BY il.InvoiceId, t.AlbumId\n",
    "),\n",
    "CustomerPreferences AS (\n",
    "    SELECT InvoiceId, AlbumId,\n",
    "           CASE WHEN TracksPurchased = TotalTracksInAlbum THEN 'Full Album'\n",
    "                ELSE 'Individual Tracks' END AS PurchaseType\n",
    "    FROM AlbumPurchases\n",
    ")\n",
    "SELECT PurchaseType, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Customer) AS Percentage\n",
    "FROM CustomerPreferences\n",
    "GROUP BY PurchaseType;\n",
    "\"\"\"\n",
    "\n",
    "# Read data into a Pandas DataFrame\n",
    "purchase_preferences = pd.read_sql_query(query, conn)\n",
    "\n",
    "# Display results\n",
    "print(purchase_preferences)"
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
