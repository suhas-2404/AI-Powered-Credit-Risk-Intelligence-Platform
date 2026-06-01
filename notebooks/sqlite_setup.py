{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "094ef9ca-2d38-4fff-b914-a4b407cabd8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import sqlite3\n",
    "\n",
    "df = pd.read_csv(\"../data/processed/train_cleaned.csv\")\n",
    "\n",
    "conn = sqlite3.connect(\"../sql/credit_risk.db\")\n",
    "\n",
    "df.to_sql(\n",
    "    \"credit_data\",\n",
    "    conn,\n",
    "    if_exists=\"replace\",\n",
    "    index=False\n",
    ")\n",
    "\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6e9834fb-02ee-4297-a620-4c94bba0ba4f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>COUNT(*)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>307511</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   COUNT(*)\n",
       "0    307511"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import sqlite3\n",
    "import pandas as pd\n",
    "\n",
    "conn = sqlite3.connect(\"../sql/credit_risk.db\")\n",
    "\n",
    "query = \"\"\"\n",
    "SELECT COUNT(*)\n",
    "FROM credit_data\n",
    "\"\"\"\n",
    "\n",
    "pd.read_sql(query, conn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "57a0e19f-3d25-40a4-b6f1-a5c438e3891b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   TOTAL_RECORDS\n",
      "0         307511\n"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "import pandas as pd\n",
    "\n",
    "conn = sqlite3.connect(\"../sql/credit_risk.db\")\n",
    "\n",
    "query = \"\"\"\n",
    "SELECT COUNT(*) AS TOTAL_RECORDS\n",
    "FROM credit_data\n",
    "\"\"\"\n",
    "\n",
    "result = pd.read_sql(query, conn)\n",
    "\n",
    "print(result)\n",
    "\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d3a07ac-ff1b-4eb1-bf12-fbd82fb73335",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
