def keyword_check(text, role):
    role_keywords = {
        "Data Scientist": ["Python", "Pandas", "ML", "statistics", "SQL", "model", "EDA"],
        "Software Engineer": ["Java", "Git", "REST", "CI/CD", "Agile", "Unit Test"],
        "Product Manager": ["roadmap", "strategy", "stakeholders", "requirements", "metrics"]
    }
    found = [kw for kw in role_keywords[role] if kw.lower() in text.lower()]
    missing = list(set(role_keywords[role]) - set(found))
    return found, missing

def grammar_check(text):
    errors = []
    if "i am" in text.lower(): errors.append("Use 'I am' instead of 'i am'")
    if "experiance" in text.lower(): errors.append("Typo: 'experiance' → 'experience'")
    return errors
