import openai
import streamlit as st

# Function to generate diverse interview questions
def generate_questions(job_title, company, job_description, past_questions):
    prompt = f"""
    You are an AI that generates diverse interview questions for a candidate applying for a job.
    The questions should cover different areas, skills, and competencies required for the role.
    
    Job Title: {job_title}
    Company: {company}
    Job Description: {job_description}

    Previous questions asked (to avoid repetition): {past_questions}

    Generate a new, unique, and varied interview question that has not been asked before:
    
    Question:
    """

    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert HR interviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9  # Increase randomness for variety
    )
    
    return response.choices[0].message.content.strip()

# Function to evaluate the user's response
def evaluate_response(question, user_response):
    prompt = f"""
    You are an AI interviewer evaluating a candidate's response to an interview question.
    
    **Interview Question:** {question}
    **Candidate's Response:** {user_response}

    Please rate the response out of 5 stars and provide concise feedback. 
    Format your response as:

    Score: X/5  
    Feedback: [Your feedback]
    """

    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert HR interviewer providing evaluations."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    
    return response.choices[0].message.content.strip()

# Initialize session state
if "question" not in st.session_state:
    st.session_state.question = None
if "evaluation" not in st.session_state:
    st.session_state.evaluation = None
if "past_questions" not in st.session_state:
    st.session_state.past_questions = []  # Store past questions

# Streamlit UI
st.title("Interview Prep Assistant")

job_title = st.text_input("Job Title", placeholder="e.g., Software Engineer")
company = st.text_input("Company", placeholder="e.g., OpenAI")
job_description = st.text_area("Job Description", placeholder="Paste the job description here")

if st.button("Generate Question"):
    if job_title and company and job_description:
        with st.spinner("Generating question..."):
            new_question = generate_questions(job_title, company, job_description, st.session_state.past_questions)
            st.session_state.past_questions.append(new_question)  # Save question history
            st.session_state.question = new_question
            st.session_state.evaluation = None  # Reset evaluation
            st.rerun()  # 🔥 Force UI refresh
    else:
        st.warning("Please fill out all fields before generating a question.")

# Show the question if it exists
if st.session_state.question:
    st.subheader("Practice Interview Question:")
    st.write(st.session_state.question)

    # User inputs their response
    user_response = st.text_area("Your Answer:")

    if st.button("Submit Answer"):
        if user_response.strip():
            with st.spinner("Evaluating your response..."):
                st.session_state.evaluation = evaluate_response(st.session_state.question, user_response)

    # Show evaluation only if it has been generated
    if st.session_state.evaluation:
        st.subheader("Evaluation:")
        st.write(st.session_state.evaluation)

    # "Next Question" button - placed BELOW the answer submission
    if st.button("Next Question"):
        with st.spinner("Generating new question..."):
            new_question = generate_questions(job_title, company, job_description, st.session_state.past_questions)
            st.session_state.past_questions.append(new_question)  # Save question history
            st.session_state.question = new_question
            st.session_state.evaluation = None  # Reset evaluation
            st.rerun()  # 🔥 Force UI refresh to immediately show the new question
