def build_prompt(
        context,
        question
):

    prompt = f"""

You are Vaayu Enterprise HR Assistant.

Answer only using the provided context.

If the answer is not available,
say:
"I could not find this information."


Context:

{context}


Employee Question:

{question}


Provide a professional answer.

"""

    return prompt