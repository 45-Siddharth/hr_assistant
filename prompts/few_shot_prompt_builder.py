from pathlib import Path


def load_examples():

    path = Path(
        "prompts/few_shot_examples.txt"
    )

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()



def build_few_shot_prompt(
        context,
        question
):

    examples = load_examples()


    prompt = f"""

You are Vaayu Enterprise HR Assistant.

Follow these rules:

1. Answer only using provided context.
2. Never invent policies.
3. Maintain professional tone.
4. Always follow the response format.


Few Shot Examples:

{examples}



Company Context:

{context}



Employee Question:

{question}



Provide response:


"""


    return prompt