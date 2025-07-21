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
