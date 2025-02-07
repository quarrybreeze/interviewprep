# 🎤 Interview Prep Assistant

📌 **Overview**  
The **Interview Prep Assistant** is a **Streamlit-based** web application that helps job seekers **practice for interviews**.  
It generates **diverse interview questions** based on the job title, company, and job description provided by the user.  
The app then evaluates user responses using **OpenAI's GPT-4o-mini** model and provides **constructive feedback**.  

---

## 🚀 Features  
✅ **Dynamic Question Generation** – Generates **unique** interview questions tailored to the job.  
✅ **Avoids Repetition** – Keeps track of **previously asked questions** to ensure variety.  
✅ **Automated Response Evaluation** – Scores user responses and provides **concise feedback**.  
✅ **User-Friendly Interface** – Built with **Streamlit** for an **interactive and intuitive experience**.  
✅ **Session Persistence** – Keeps previous questions and evaluations accessible **within the session**.  

---

## 🛠 Technologies Used  
🔹 **Python** – Core programming language.  
🔹 **Streamlit** – Web framework for building the app.  
🔹 **OpenAI API (GPT-4o-mini)** – For question generation & response evaluation.  

---

## 🔧 Installation  

### 📌 **Prerequisites**  
- 🐍 **Python 3.8+** installed  
- 🔑 **An OpenAI API key**  
- 🎛️ **Streamlit library installed**  

---

## 📥 **Setup Instructions**  

**1️⃣ Clone this repository**  
```sh
git clone https://github.com/your-repo/interview-prep-assistant.git
cd interview-prep-assistant
```
2️⃣ Install dependencies
```sh
pip install -r requirements.txt
```
3️⃣ Set up your OpenAI API key

Create a .streamlit/secrets.toml file and add your API key:

```toml
[openai]
api_key = "your_api_key_here"
```
4️⃣ Run the application in terminal
```sh
streamlit run app.py
```
---

## 🎯 Usage

📌 To practice your interview skills, follow these steps:

1️⃣ Enter the Job Title, Company, and Job Description in the input fields.  
2️⃣ Click "Generate Question" to receive a unique interview question.  
3️⃣ Type your answer in the provided text area.  
4️⃣ Click "Submit Answer" to get a score and feedback.  
5️⃣ Click "Next Question" to receive another question.  
6️⃣ Click "Clear Answer" to reset your response.  
