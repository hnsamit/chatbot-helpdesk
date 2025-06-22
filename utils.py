import json

def load_faqs():
    with open("faq_data.json", "r") as f:
        return json.load(f)

def match_faq(user_question, faqs):
    for faq in faqs:
        if faq["question"].lower() in user_question.lower():
            return faq["answer"]
    return None
