{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "09f9b4ee-0efd-46cb-837d-09809a66a535",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: pandas in /home/suhas/.local/lib/python3.10/site-packages (2.3.3)\n",
      "Requirement already satisfied: numpy in /home/suhas/.local/lib/python3.10/site-packages (1.23.5)\n",
      "Requirement already satisfied: matplotlib in /home/suhas/.local/lib/python3.10/site-packages (3.10.9)\n",
      "Requirement already satisfied: seaborn in /home/suhas/.local/lib/python3.10/site-packages (0.13.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in /usr/lib/python3/dist-packages (from pandas) (2022.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in /home/suhas/.local/lib/python3.10/site-packages (from pandas) (2025.3)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /home/suhas/.local/lib/python3.10/site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in /home/suhas/.local/lib/python3.10/site-packages (from matplotlib) (1.3.2)\n",
      "Requirement already satisfied: packaging>=20.0 in /home/suhas/.local/lib/python3.10/site-packages (from matplotlib) (26.0)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in /home/suhas/.local/lib/python3.10/site-packages (from matplotlib) (4.63.0)\n",
      "Requirement already satisfied: cycler>=0.10 in /home/suhas/.local/lib/python3.10/site-packages (from matplotlib) (0.12.1)\n",
      "Requirement already satisfied: kiwisolver>=1.3.1 in /home/suhas/.local/lib/python3.10/site-packages (from matplotlib) (1.5.0)\n",
      "Requirement already satisfied: pyparsing>=3 in /home/suhas/.local/lib/python3.10/site-packages (from matplotlib) (3.3.2)\n",
      "Requirement already satisfied: pillow>=8 in /home/suhas/.local/lib/python3.10/site-packages (from matplotlib) (12.1.0)\n",
      "Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas numpy matplotlib seaborn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8aa206aa-877b-4281-9339-9b7c4be2bd1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(307511, 122)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv(\"../data/raw/application_train.csv\")\n",
    "\n",
    "print(df.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bd91b1e0-b737-4632-bd82-d33c5f8a5bc3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape: (307511, 122)\n",
      "\n",
      "Data Types:\n",
      "float64    65\n",
      "int64      41\n",
      "object     16\n",
      "Name: count, dtype: int64\n",
      "\n",
      "Missing Values:\n",
      "COMMONAREA_MEDI             214865\n",
      "COMMONAREA_AVG              214865\n",
      "COMMONAREA_MODE             214865\n",
      "NONLIVINGAPARTMENTS_MODE    213514\n",
      "NONLIVINGAPARTMENTS_AVG     213514\n",
      "NONLIVINGAPARTMENTS_MEDI    213514\n",
      "FONDKAPREMONT_MODE          210295\n",
      "LIVINGAPARTMENTS_MODE       210199\n",
      "LIVINGAPARTMENTS_AVG        210199\n",
      "LIVINGAPARTMENTS_MEDI       210199\n",
      "FLOORSMIN_AVG               208642\n",
      "FLOORSMIN_MODE              208642\n",
      "FLOORSMIN_MEDI              208642\n",
      "YEARS_BUILD_MEDI            204488\n",
      "YEARS_BUILD_MODE            204488\n",
      "YEARS_BUILD_AVG             204488\n",
      "OWN_CAR_AGE                 202929\n",
      "LANDAREA_MEDI               182590\n",
      "LANDAREA_MODE               182590\n",
      "LANDAREA_AVG                182590\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(\"Shape:\", df.shape)\n",
    "\n",
    "print(\"\\nData Types:\")\n",
    "print(df.dtypes.value_counts())\n",
    "\n",
    "print(\"\\nMissing Values:\")\n",
    "print(df.isnull().sum().sort_values(ascending=False).head(20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "503fb3a8-594e-4a9d-8da0-51ef327d42e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "TARGET\n",
       "0    282686\n",
       "1     24825\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"TARGET\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "04052d8a-f7e2-4795-a82c-4ca4b90a4bea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "TARGET\n",
       "0    91.927118\n",
       "1     8.072882\n",
       "Name: proportion, dtype: float64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"TARGET\"].value_counts(normalize=True) * 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "20ba93a0-1ca0-472c-a604-f077b1d8fcc8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    307511.000000\n",
       "mean         43.936973\n",
       "std          11.956133\n",
       "min          20.517808\n",
       "25%          34.008219\n",
       "50%          43.150685\n",
       "75%          53.923288\n",
       "max          69.120548\n",
       "Name: AGE, dtype: float64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"AGE\"] = abs(df[\"DAYS_BIRTH\"]) / 365\n",
    "\n",
    "df[\"AGE\"].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b97b7dac-499b-4806-af2d-a8011a6a7073",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAskAAAHWCAYAAACFXRQ+AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjksIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvJkbTWQAAAAlwSFlzAAAPYQAAD2EBqD+naQAAS71JREFUeJzt3XtYVWX+///XRuTggZPIqUCpTDxrWoRmaZJo1mSZk6mlaToZWOpMmY15ahpL86yj40xmfcIsZ9IxSxO1tEZCxUgxNC0NRwUjBTwgB1m/P/qyfu6FmsKWvZHn47r2dbnX/d73fi+WdL1crXUvm2EYhgAAAACY3JzdAAAAAOBqCMkAAACABSEZAAAAsCAkAwAAABaEZAAAAMCCkAwAAABYEJIBAAAAC0IyAAAAYEFIBgAAACwIyQBqHJvNpkmTJpnvly5dKpvNpkOHDjmtp5rOekyulS+++EI2m01ffPGFua1Lly5q2bLlNf9uSTp06JBsNpuWLl1aJd8HoOIIyQCc5m9/+5tsNpuio6Od3YpLOHv2rCZNmmQX4K7Up59+KpvNprCwMJWWljq+uavQuHFj2Ww22Ww2ubm5yc/PT61atdLw4cOVkpLisO9ZtmyZZs+e7bD5HMmVewNwZWyGYRjObgJAzdSpUycdPXpUhw4d0v79+3XLLbdUyffabDZNnDjRPHN5/vx5FRcXy9PTUzabrUp6uJicnBw1bNjQrrcrNWDAAG3dulWHDh1SUlKSYmNjr02TV6Bx48by9/fXH//4R0nSqVOnlJGRoRUrVigrK0ujR4/WzJkz7T5z7tw5ubu7y93d/Yq/54EHHlB6evpV/R+A0tJSFRUVycPDQ25uv54n6tKli3JycpSenn7F81S0N8MwVFhYqNq1a6tWrVoO+z4AjseZZABOcfDgQW3dulUzZ85Uw4YNlZiY6LReatWqJS8vL6cG5Mo4c+aM/vOf/2jMmDFq166dU3+WZW644QYNHDhQAwcO1IgRIzR37lz9+OOP6t27t2bNmqWFCxfa1Xt5eV1VQL5a586dU2lpqdzc3OTl5WUG5Kpms9nk5eVFQAaqAUIyAKdITEyUv7+/evXqpUcfffSiwa7s+s0333xTs2bNUqNGjeTt7a177rmn3Fm/wYMHq169evrxxx8VFxenunXrKiwsTFOmTNFv/Q+zS12TvHbtWt1zzz2qX7++fHx8dPvtt2vZsmXm+Jdffqm+ffsqIiJCnp6eCg8P1+jRo1VQUHDR3o4cOaLevXurXr16atiwof70pz/p/Pnz5r42bNhQkjR58mTzcoUrOaO8cuVKFRQUqG/fvurXr58++ugjnTt3rlxdQUGBnnvuOQUGBqp+/fr63e9+pyNHjlz0e44cOaIhQ4YoODhYnp6eatGihZYsWfKbvVyOt7e3/u///k8BAQF67bXX7I6LtYdTp05p1KhRaty4sTw9PRUUFKT77rtPO3fulPTr2d9PPvlEP/30k/mzaty4saT//7rj5cuXa/z48brhhhtUp04d5efnX/Sa5DKpqanq2LGjvL29FRkZqUWLFtmNX+rviXXOy/V2qWuSN23apM6dO6tu3bry8/PTQw89pIyMDLuaSZMmyWaz6cCBAxo8eLD8/Pzk6+urp556SmfPnr2ygwDgil27f7YDwGUkJibqkUcekYeHhx5//HEtXLhQ27dv1+23316u9t1339WpU6cUHx+vc+fOac6cObr33nu1e/duBQcHm3Xnz59Xjx49dOedd2ratGlat26dJk6cqJKSEk2ZMuWq+lu6dKmGDBmiFi1aaNy4cfLz89M333yjdevWqX///pKkFStW6OzZsxoxYoQaNGigbdu2ad68efrf//6nFStW2M13/vx5xcXFKTo6Wm+++aY2bNigGTNm6Oabb9aIESPUsGFDLVy4UCNGjNDDDz+sRx55RJLUunXrK/pZdu3aVSEhIerXr59eeuklffzxx+rbt69d3eDBg/Xhhx/qiSee0J133qnNmzerV69e5ebLzs7WnXfeKZvNpoSEBDVs2FBr167V0KFDlZ+fr1GjRl3Vz/JC9erV08MPP6y33npL3333nVq0aHHRumeeeUb/+te/lJCQoObNm+uXX37RV199pYyMDN12223685//rLy8PP3vf//TrFmzzLkv9Oqrr8rDw0N/+tOfVFhYKA8Pj0v2dfLkSd1///36/e9/r8cff1wffvihRowYIQ8PDw0ZMuSq9vFKervQhg0b1LNnT910002aNGmSCgoKNG/ePHXq1Ek7d+40A3aZ3//+94qMjNTUqVO1c+dO/fOf/1RQUJDeeOONq+oTwG8wAKCK7dixw5BkJCUlGYZhGKWlpcaNN95oPP/883Z1Bw8eNCQZ3t7exv/+9z9ze0pKiiHJGD16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T5/WBx98oB07digrK0tLly7Vyy+/LEmaNWuWvvrqK+3YsUPt2rUzPxMREaF77rlH1nMqnp6eCgkJqdL+AaCqcLkFANQgH374oaKiotS0aVMNHDhQS5YsMcPv+++/r/vuu88uIF/IZrNVZasA4FSEZACoQd566y0NHDhQktSjRw/l5eVp8+bNkqTvv/9eTZs2tat/+OGHVa9ePdWrV08dO3a0G1uzZo05Vvb661//WjU7AgDXGJdbAEANsW/fPm3btk0rV66UJLm7u+uxxx7TW2+9pS5dulz0M3/729905swZzZ07V1u2bLEb69q1qxYuXGi3LSAg4Jr0DgBVjZAMADXEW2+9pZKSEvNGPUkyDEOenp6aP3++mjRpon379tl9JjQ0VNLFw2/dunV1yy23XNumAcBJuNwCAGqAkpISvfvuu5oxY4bS0tLM17fffquwsDC9//77evzxx5WUlKRvvvnG2e0CgNNxJhkAaoA1a9bo5MmTGjp0qHx9fe3G+vTpo7feektffvmlPvnkE3Xr1k0TJ05U586d5e/vr++//15r165VrVq17D5XWFiorKwsu23u7u4KDAy85vsDANca6yQDQA3w4IMPqrS0VJ988km5sW3btik6OlrffvutmjZtqtmzZ+v999/X999/r9LSUkVGRqpnz54aPXq0wsPDJf26TvI777xTbq6mTZtq796913x/AOBaIyQDAAAAFlyTDAAAAFgQkgEAAAALQjIAAABgQUgGAAAALAjJAAAAgAUhGQAAALAgJAMAAAAWhGQAAADAgpAMAAAAWBCSAQAAAAtCMgAAAGDx/wHEwoRgljcqrwAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 800x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "plt.figure(figsize=(8,5))\n",
    "sns.histplot(df[\"AGE\"], bins=30)\n",
    "plt.title(\"Applicant Age Distribution\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b81c43f6-5447-45bd-a69f-8f2681259950",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TARGET                0          1\n",
      "CODE_GENDER                       \n",
      "F             93.000672   6.999328\n",
      "M             89.858080  10.141920\n",
      "XNA          100.000000   0.000000\n"
     ]
    }
   ],
   "source": [
    "gender_default = pd.crosstab(\n",
    "    df[\"CODE_GENDER\"],\n",
    "    df[\"TARGET\"],\n",
    "    normalize=\"index\"\n",
    ") * 100\n",
    "\n",
    "print(gender_default)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fe5df22c-b9a8-4e98-ad7f-66a3649ae573",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TARGET\n",
      "0    169077.722266\n",
      "1    165611.760906\n",
      "Name: AMT_INCOME_TOTAL, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "income_default = df.groupby(\"TARGET\")[\"AMT_INCOME_TOTAL\"].mean()\n",
    "\n",
    "print(income_default)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "96d9df43-8d85-4852-a1c8-97be383bba40",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TARGET                                 0          1\n",
      "NAME_EDUCATION_TYPE                                \n",
      "Academic degree                98.170732   1.829268\n",
      "Higher education               94.644885   5.355115\n",
      "Incomplete higher              91.515034   8.484966\n",
      "Lower secondary                89.072327  10.927673\n",
      "Secondary / secondary special  91.060071   8.939929\n"
     ]
    }
   ],
   "source": [
    "education_default = pd.crosstab(\n",
    "    df[\"NAME_EDUCATION_TYPE\"],\n",
    "    df[\"TARGET\"],\n",
    "    normalize=\"index\"\n",
    ") * 100\n",
    "\n",
    "print(education_default)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3e3f6f07-03ac-4707-9fa1-d5192367b66d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'sklearn.pipeline.Pipeline'>\n"
     ]
    }
   ],
   "source": [
    "import joblib\n",
    "\n",
    "model = joblib.load(\"../models/credit_risk_model.pkl\")\n",
    "\n",
    "print(type(model))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7b4213af-020b-4da1-a75e-6fbda9fea618",
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
