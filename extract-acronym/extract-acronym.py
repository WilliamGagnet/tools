import re
import pandas as pd
import json

def extract_acronyms(text):
    # regex search for words with 2+ uppercase letters
    return re.findall(r"\b[A-Z]{2,}\b", text)

def print_acronyms(data):
    all_questions = []
    for domain, questions in data.items():
        for q in questions:
            all_questions.append(q)
    df = pd.DataFrame(all_questions)

    acronyms = set()

    for q in df["question"]:
        acronyms.update(extract_acronyms(q))

    for y in df["yes_attribute"]:
        acronyms.update(extract_acronyms(y))

    for n in df["no_attribute"]:
        acronyms.update(extract_acronyms(n))

    for r in df["remediation"]:
        for step in r:
            acronyms.update(extract_acronyms(step))

    print(sorted(acronyms))

def fix_text(text):
    if not text:
        raise ValueError("Empty string found")
    
    matches = list(re.finditer(r"\b[A-Z]{2,}\b", text)) # find the locations of acronyms using regex 
    text = text.lower() # make is all lower case
    
    for match in matches: # each acronym
        start, end = match.span()
        text = text[:start] + text[start:end].upper() + text[end:] # capitalize acronym

    text = text[0].upper() + text[1:] # capitalize start of sentence
    return text

def main():
    mode = "product"

    if mode == "home":
        with open("wizard_questions.json", "r", encoding="utf-8") as f:
            data = json.load(f) # external file of all home questions and their associated info
    if mode == "enterprise":
        with open("wizard_questions_enterprise.json", "r", encoding="utf-8") as f:
            data = json.load(f) # external file of all enterprise questions and their associated info
    if mode == "product":
        with open("wizard_questions_product.json", "r", encoding="utf-8") as f:
            data = json.load(f) # external file of all product questions and their associated info

    print_acronyms(data)

    for domain, questions in data.items(): # each domain
        for q in questions: # each question
            attributes = ["question", "yes_attribute", "no_attribute"]
            for attr in attributes: # each attribute
                q[attr] = fix_text(q[attr])

            q["remediation"] = [fix_text(step) for step in q["remediation"]] # remediation steps

    output_name = f"output_{mode}.json"
    with open(output_name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()