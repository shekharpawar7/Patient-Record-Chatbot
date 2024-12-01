import os
import csv
import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_TOKEN")

# Initialize Flask app
app = Flask(__name__)

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
        prompt = f"Here is a dataset of patient records:\n\n{json_data}\n\nUser question: {question}\nProvide a ONE LINE answer based on the patient data above."

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

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_query = request.form["query"]
        csv_file_path = "C:\\Users\\shekhar\\Downloads\\vitals.csv"  # Update with your CSV path
        
        # Convert the CSV to JSON (in-memory)
        json_data = csv_to_json_in_memory(csv_file_path)
        
        if not json_data:
            return render_template("index.html", answer="No data available in the CSV file.")
        
        # Process the user query
        answer = process_patient_query(user_query, json_data)
        return render_template("index.html", answer=answer)
    
    return render_template("index.html", answer=None)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
