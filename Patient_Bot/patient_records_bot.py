import os
import csv
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Your OpenAI API Key from environment variable
openai.api_key = os.environ.get("OPENAI_API_TOKEN")

# Function to convert CSV to JSON (in-memory)
def csv_to_json_in_memory(csv_file_path):
    try:
        # Read the CSV file
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]  # Store CSV data as a list of dictionaries
        return data
    except Exception as e:
        print(f"Error converting CSV to JSON: {str(e)}")
        return []

# Function to process a question related to the patient data
def process_patient_query(question, json_data):
    try:
        # Create a prompt to send to OpenAI
        prompt = f"Here is a dataset of patient records:\n\n{json_data}\n\nUser question: {question}\nProvide a detailed answer based on the patient data above."

        # Use OpenAI's API to generate a response
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  # Use GPT-3.5
            prompt=prompt,
            temperature=0.7,
            max_tokens=150,
            n=1,
            stop=None
        )
        
        # Return the generated answer
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error processing the question: {str(e)}"

# Function to handle user input and questions
def handle_user_query():
    try:
        # Path to your CSV file
        csv_file_path = "C:\\Users\\shekhar\\Downloads\\vitals.csv"  # Update with your path
        
        # Convert the CSV to JSON (in-memory)
        json_data = csv_to_json_in_memory(csv_file_path)
        
        if not json_data:
            print("No data available in the CSV file.")
            return

        while True:
            # Taking user input (query)
            user_query = input("Ask a question related to the patient records (or type 'exit' to quit): ").strip()

            if user_query.lower() == "exit":
                print("Goodbye!")
                break

            # Process the query and get the response from AI model
            answer = process_patient_query(user_query, json_data)
            print("Answer:", answer)

    except Exception as e:
        print(f"Error: {str(e)}")

# Start the chatbot
if __name__ == "__main__":
    handle_user_query()
