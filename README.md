# JU21-Resume-Validator-AI
Gen AI

🧠 Project Title: Resume Validator AI
A smart AI system that allows users to upload resumes and get a validation report based on job role fitment, missing keywords, grammar issues, and suggestions using LLM and static checks.

✅ Features
Upload a .pdf or .docx resume

Extract and analyze resume content

Match it against selected job roles

Highlight missing skills, keywords, grammar errors

Generate suggestions via LLM

Download the full validation report

🗂️ Folder Structure
bash
Copy
Edit
resume-validator-ai/
├── app.py                   # Streamlit app
├── agent/
│   └── validator_agent.py   # Orchestrates validation via rules and LLM
├── utils/
│   ├── extract.py           # Resume text extraction
│   ├── rules.py             # Static checks (keywords, grammar)
│   └── llm_feedback.py      # Feedback generation from LLM
└── samples/
    └── sample_resume.pdf    # Sample resume for testing
💡 Setup Instructions
Clone repo or copy files.

Install dependencies:

bash
Copy
Edit
pip install streamlit python-docx PyPDF2 openai
Add your OpenAI key (if using GPT):

bash
Copy
Edit
export OPENAI_API_KEY=your_key_here
Run:

bash
Copy
Edit
streamlit run app.py
