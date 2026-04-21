import re
import pandas as pd
import json

def extract_acronyms(text):
    # words with 2+ uppercase letters
    return re.findall(r"\b[A-Z]{2,}\b", text)

mode = "home"

if mode == "home":
    with open("wizard_questions.json", "r", encoding="utf-8") as f:
        data = json.load(f) # external file of all home questions and their associated info
if mode == "enterprise":
    with open("wizard_questions_enterprise.json", "r", encoding="utf-8") as f:
        data = json.load(f) # external file of all enterprise questions and their associated info
if mode == "product":
    with open("wizard_questions_product.json", "r", encoding="utf-8") as f:
        data = json.load(f) # external file of all product questions and their associated info

all_questions = []
for domain, questions in data.items():
    for q in questions:
        all_questions.append(q)
df = pd.DataFrame(all_questions)

acronyms = set()

for q in df["question"]:
    acronyms.update(extract_acronyms(q))

for r in df["remediation"]:
    acronyms.update(extract_acronyms(r))

print(sorted(acronyms))
