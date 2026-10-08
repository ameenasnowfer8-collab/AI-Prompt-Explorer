def simple_prompt(topic):
    return f"Give a short and clear explanation of {topic}."


def expert_prompt(topic):
    return f"""
Act as an expert teacher and explain {topic}.

Your response should include:
1. Introduction
2. Important concepts
3. Real-world example
4. Benefits
5. Summary

Use clear and understandable language.
"""


def question_answer_prompt(topic):
    return f"""
Explain {topic} in a question-and-answer format.

Include:
Q1. What is {topic}?
Q2. Why is it important?
Q3. How does it work?
Q4. Give a real-world example.
Q5. What are its benefits?

Provide clear answers for each question.
"""


def generate_prompts(topic):
    return {
        "Simple Prompt": simple_prompt(topic),
        "Expert Prompt": expert_prompt(topic),
        "Q&A Prompt": question_answer_prompt(topic)
    }