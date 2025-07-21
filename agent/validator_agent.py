from utils.rules import keyword_check, grammar_check
from utils.llm_feedback import generate_llm_feedback

def validate_resume(text, role):
    found, missing = keyword_check(text, role)
    grammar_issues = grammar_check(text)
    llm_feedback = generate_llm_feedback(text, role)

    report = f"""
🔎 **Keyword Match for '{role}'**
- ✅ Found: {', '.join(found)}
- ❌ Missing: {', '.join(missing) if missing else 'None'}

✍️ **Grammar Suggestions**
{'\n'.join(f'- {issue}' for issue in grammar_issues) if grammar_issues else '✔️ No grammar issues found.'}

🤖 **LLM Feedback**
{llm_feedback}
"""
    return report
