Interview Prep Assistant

Overview

The Interview Prep Assistant is a Streamlit-based web application that helps job seekers practice for interviews. It generates diverse interview questions based on the job title, company, and job description provided by the user. The app evaluates user responses using OpenAI's GPT-4o-mini model and provides constructive feedback.

Features

Dynamic Question Generation: Generates unique interview questions tailored to the job title, company, and job description.

Avoids Repetition: Keeps track of previously asked questions to ensure variety.

Automated Response Evaluation: Scores user responses and provides concise feedback.

User-Friendly Interface: Built with Streamlit for an interactive and intuitive experience.

Technologies Used

Python

Streamlit

OpenAI API (GPT-4o-mini)

Installation

Prerequisites

Python 3.8+

An OpenAI API key

Streamlit library installed

Setup Instructions

Clone this repository:

git clone https://github.com/your-repo/interview-prep-assistant.git
cd interview-prep-assistant

Install dependencies:

pip install -r requirements.txt

Create a .streamlit/secrets.toml file and add your OpenAI API key:

[openai]
api_key = "your_api_key_here"

Run the application:

streamlit run app.py

Usage

Enter the Job Title, Company, and Job Description in the input fields.

Click "Generate Question" to receive a unique interview question.

Type your answer in the text area provided.

Click "Submit Answer" to get a score and feedback.

Click "Next Question" to receive another question.