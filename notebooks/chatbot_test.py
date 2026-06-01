import os
from queue import Full


{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d7ff0a32-8a57-4382-aa46-6f3a1f578e8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: google-generativeai in /home/suhas/.local/lib/python3.10/site-packages (0.8.6)\n",
      "Requirement already satisfied: protobuf in /home/suhas/.local/lib/python3.10/site-packages (from google-generativeai) (5.29.6)\n",
      "Requirement already satisfied: google-ai-generativelanguage==0.6.15 in /home/suhas/.local/lib/python3.10/site-packages (from google-generativeai) (0.6.15)\n",
      "Requirement already satisfied: pydantic in /home/suhas/.local/lib/python3.10/site-packages (from google-generativeai) (2.12.5)\n",
      "Requirement already satisfied: google-api-core in /home/suhas/.local/lib/python3.10/site-packages (from google-generativeai) (2.30.3)\n",
      "Requirement already satisfied: google-auth>=2.15.0 in /home/suhas/.local/lib/python3.10/site-packages (from google-generativeai) (2.48.0)\n",
      "Requirement already satisfied: typing-extensions in /home/suhas/.local/lib/python3.10/site-packages (from google-generativeai) (4.15.0)\n",
      "Requirement already satisfied: google-api-python-client in /home/suhas/.local/lib/python3.10/site-packages (from google-generativeai) (2.197.0)\n",
      "Requirement already satisfied: tqdm in /home/suhas/.local/lib/python3.10/site-packages (from google-generativeai) (4.67.3)\n",
      "Requirement already satisfied: proto-plus<2.0.0dev,>=1.22.3 in /home/suhas/.local/lib/python3.10/site-packages (from google-ai-generativelanguage==0.6.15->google-generativeai) (1.28.0)\n",
      "Requirement already satisfied: rsa<5,>=3.1.4 in /home/suhas/.local/lib/python3.10/site-packages (from google-auth>=2.15.0->google-generativeai) (4.9.1)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/lib/python3/dist-packages (from google-auth>=2.15.0->google-generativeai) (0.2.1)\n",
      "Requirement already satisfied: cryptography>=38.0.3 in /home/suhas/.local/lib/python3.10/site-packages (from google-auth>=2.15.0->google-generativeai) (46.0.4)\n",
      "Requirement already satisfied: googleapis-common-protos<2.0.0,>=1.63.2 in /home/suhas/.local/lib/python3.10/site-packages (from google-api-core->google-generativeai) (1.75.0)\n",
      "Requirement already satisfied: requests<3.0.0,>=2.20.0 in /home/suhas/.local/lib/python3.10/site-packages (from google-api-core->google-generativeai) (2.32.5)\n",
      "Requirement already satisfied: uritemplate<5,>=3.0.1 in /home/suhas/.local/lib/python3.10/site-packages (from google-api-python-client->google-generativeai) (4.2.0)\n",
      "Requirement already satisfied: httplib2<1.0.0,>=0.19.0 in /usr/lib/python3/dist-packages (from google-api-python-client->google-generativeai) (0.20.2)\n",
      "Requirement already satisfied: google-auth-httplib2<1.0.0,>=0.2.0 in /home/suhas/.local/lib/python3.10/site-packages (from google-api-python-client->google-generativeai) (0.4.0)\n",
      "Requirement already satisfied: pydantic-core==2.41.5 in /home/suhas/.local/lib/python3.10/site-packages (from pydantic->google-generativeai) (2.41.5)\n",
      "Requirement already satisfied: typing-inspection>=0.4.2 in /home/suhas/.local/lib/python3.10/site-packages (from pydantic->google-generativeai) (0.4.2)\n",
      "Requirement already satisfied: annotated-types>=0.6.0 in /home/suhas/.local/lib/python3.10/site-packages (from pydantic->google-generativeai) (0.7.0)\n",
      "Requirement already satisfied: cffi>=2.0.0 in /home/suhas/.local/lib/python3.10/site-packages (from cryptography>=38.0.3->google-auth>=2.15.0->google-generativeai) (2.0.0)\n",
      "Requirement already satisfied: grpcio<2.0.0,>=1.33.2 in /home/suhas/.local/lib/python3.10/site-packages (from google-api-core->google-generativeai) (1.78.0)\n",
      "Requirement already satisfied: grpcio-status<2.0.0,>=1.33.2 in /home/suhas/.local/lib/python3.10/site-packages (from google-api-core->google-generativeai) (1.71.2)\n",
      "Requirement already satisfied: pyparsing!=3.0.0,!=3.0.1,!=3.0.2,!=3.0.3,<4,>=2.4.2 in /home/suhas/.local/lib/python3.10/site-packages (from httplib2<1.0.0,>=0.19.0->google-api-python-client->google-generativeai) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /usr/lib/python3/dist-packages (from requests<3.0.0,>=2.20.0->google-api-core->google-generativeai) (3.3)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /home/suhas/.local/lib/python3.10/site-packages (from requests<3.0.0,>=2.20.0->google-api-core->google-generativeai) (2.6.3)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in /home/suhas/.local/lib/python3.10/site-packages (from requests<3.0.0,>=2.20.0->google-api-core->google-generativeai) (3.4.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests<3.0.0,>=2.20.0->google-api-core->google-generativeai) (2020.6.20)\n",
      "Requirement already satisfied: pyasn1>=0.1.3 in /usr/lib/python3/dist-packages (from rsa<5,>=3.1.4->google-auth>=2.15.0->google-generativeai) (0.4.8)\n",
      "Requirement already satisfied: pycparser in /home/suhas/.local/lib/python3.10/site-packages (from cffi>=2.0.0->cryptography>=38.0.3->google-auth>=2.15.0->google-generativeai) (3.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install google-generativeai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "420fa000-fbcc-4d06-a7d2-059513dda03e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "import os\n",
    "\n",
    "sys.path.append(os.path.abspath(\"..\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "84450aa4-e246-40e2-a7e1-51473e56fd54",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: python-dotenv in /home/suhas/.local/lib/python3.10/site-packages (1.2.2)\n"
     ]
    }
   ],
   "source": [
    "!pip install python-dotenv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "08a7a3c7-2b54-4bae-9f61-a721e67b90e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Import successful\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "import os\n",
    "\n",
    "sys.path.append(os.path.abspath(\"..\"))\n",
    "\n",
    "from src.talk_to_data.nl_to_sql import generate_sql\n",
    "\n",
    "print(\"Import successful\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "79e0d8fe-065a-4c35-ad3a-aa2305bda46f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      os.getenv("GEMINI_API_KEY")
     ]
    }
   ],
   "source": [
    "from dotenv import load_dotenv\n",
    "import os\n",
    "\n",
    "load_dotenv(\"../.env\")\n",
    "\n",
    "print(os.getenv(\"GEMINI_API_KEY\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "dd224a3b-acc2-4037-9928-803c43710651",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SELECT COUNT(SK_ID_CURR) FROM credit_data WHERE TARGET = 1\n"
     ]
    }
   ],
   "source": [
    "from src.talk_to_data.nl_to_sql import generate_sql\n",
    "\n",
    "question = \"How many customers defaulted?\"\n",
    "\n",
    "sql_query = generate_sql(question)\n",
    "\n",
    "print(sql_query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a1b03da1-a430-4402-a37b-96964cf6c8d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   COUNT(SK_ID_CURR)\n",
      "0              24825\n"
     ]
    }
   ],
   "source": [
    "from src.talk_to_data.query_runner import run_query\n",
    "\n",
    "result = run_query(\"\"\"\n",
    "SELECT COUNT(SK_ID_CURR)\n",
    "FROM credit_data\n",
    "WHERE TARGET = 1\n",
    "\"\"\")\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "828cfcf6-8314-4e97-9357-7761e9861035",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'SELECT AVG(AMT_INCOME_TOTAL) FROM credit_data'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "generate_sql(\n",
    "    \"What is the average income of applicants?\"\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8f34cf43-880d-433e-84c8-aebe4a690a25",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'SELECT\\n  NAME_EDUCATION_TYPE\\nFROM\\n  credit_data\\nGROUP BY\\n  NAME_EDUCATION_TYPE\\nORDER BY\\n  SUM(TARGET) * 1.0 / COUNT(TARGET) DESC\\nLIMIT 1'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "generate_sql(\n",
    "    \"Which education group has the highest default rate?\"\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "4bc3c3b7-97eb-4108-976d-13ab334879f4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'SELECT\\n  CODE_GENDER\\nFROM\\n  credit_data\\nGROUP BY\\n  CODE_GENDER\\nORDER BY\\n  CAST(SUM(TARGET) AS REAL) / COUNT(TARGET) DESC\\nLIMIT 1'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "generate_sql(\n",
    "    \"Which gender has the highest default rate?\"\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": Full,
   "id": "29ab9a5f-57ad-47d9-ae23-8a596dbfd0e3",
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
