# AI-powered Chatbot for Patient Data Queries

This repository contains a simple AI-powered chatbot system that answers queries related to patient records. The chatbot uses OpenAI's GPT-3 model to process questions regarding patient data, such as vital signs (e.g., age, blood pressure), and provides responses by leveraging data stored in a CSV file. The CSV data is converted to JSON format for easier querying and processing.

## Objective

The goal of the system is to use natural language processing (NLP) to answer user queries based on patient data stored in a CSV file. The system allows users to ask questions like:

- "What is the max age of the patient?"
- "On which date was the blood pressure high?"

### Key Features

- **CSV to JSON Conversion**: The system reads a CSV file containing patient data and converts it to a JSON format for easier querying and manipulation.
- **User-Friendly Interface**: The chatbot allows users to interact with the data using natural language queries.
- **Integration with GPT-3**: The chatbot sends queries to OpenAI's GPT-3 model and receives detailed responses based on the patient data.

## How It Works

The chatbot system consists of three main components:

1. **CSV to JSON Conversion**: Converts the CSV file to JSON in memory for efficient processing.
2. **User Query Processing**: Sends user queries to OpenAI's GPT-3 model along with relevant patient data, and processes the model's response.
3. **Interactive Query System**: A continuous loop where the chatbot accepts user queries and provides responses until the user exits.

## Getting Started

### Prerequisites
Before you can run the chatbot, ensure you have the following:

- Python 3.x
- `openai` library for GPT-3 integration
- `csv` library for reading CSV files
- An OpenAI API key (you can get it from [OpenAI](https://beta.openai.com/signup/))

### Installation

Clone this repository:
   git clone https://github.com/yourusername/chatbot-patient-records.git
   cd chatbot-patient-records
Install the required Python packages:

pip install -r requirements.txt
Create a .env file in the root directory and add your OpenAI API key:

OPENAI_API_TOKEN=your-api-key
Make sure you have a CSV file with patient records. The system expects the CSV file to have columns like Name, Age, Blood Pressure, Date, etc. You can modify the csv_file_path variable in the code to point to your CSV file.

Usage
Run the application:

python patient_records_bot.py
The chatbot will prompt you to enter a query related to the patient data. For example, you can ask:

"What is the max age of the patient?"
"On which date was the blood pressure high?"
The chatbot will process your question and provide an answer based on the available data.

Example Queries:
Query: "What is the max age of the patient?"

Response: "The oldest patient is John Doe, with an age of 85."

Query: "On which date was the blood pressure high?"

Response: "The blood pressure was high on 2024-05-22 for patient Alice Smith."

Limitations
Data Quality: The accuracy of responses depends on the quality and structure of the CSV file. Missing or incorrect data can lead to wrong answers.
Contextual Understanding: GPT-3 may not always provide precise answers without detailed prompts or context, especially for more specific questions.
Performance: As the dataset grows, in-memory processing may become less efficient, especially for large CSV files.
Conclusion
The chatbot system demonstrates a straightforward way to interact with structured patient data using natural language queries. It leverages OpenAI's GPT-3 model to answer questions based on a CSV file converted to JSON. This solution is effective for providing detailed insights from structured datasets, making it useful for various data exploration and reporting scenarios.


