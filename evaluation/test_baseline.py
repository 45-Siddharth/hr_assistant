import json

from services.openai_service import client
from core.config import AZURE_OPENAI_DEPLOYMENT

with open(
    "evaluation/evaluation_questions.json",
    "r",
    encoding="utf-8"
) as file:

    questions = json.load(file)

results = []

for item in questions:

    response = client.chat.completions.create(

        model=AZURE_OPENAI_DEPLOYMENT,

        messages=[

            {
                "role":"user",
                "content":item["question"]
            }

        ],

        temperature=0.2,
        max_completion_tokens=250
    )

    answer = response.choices[0].message.content

    results.append({

        "question": item["question"],

        "answer": answer

    })

with open(

    "evaluation/baseline_results.json",

    "w",

    encoding="utf-8"

) as file:

    json.dump(

        results,

        file,

        indent=4

    )

print("Baseline evaluation completed.")