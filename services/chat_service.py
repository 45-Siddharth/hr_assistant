from services.openai_service import client

from openai import APIError

def ask_llm(question):

    try:

        response = client.chat.completions.create(

            model="gpt-4.1-mini-2025-04-14.ft-195e36d145d84860b0b4706f696d265f",

            messages=[
                {
            "role": "system",
            "content": "You are Vaayu Enterprise HR Assistant. Answer employee HR questions professionally using company policies only."
            },
                {
                    "role":"user",
                    "content":question
                }
            ],

            temperature=0.2,

            max_completion_tokens=500

        )

        return response.choices[0].message.content

    except APIError as e:

        return f"Azure OpenAI Error: {str(e)}"

    except Exception as e:

        return f"Unexpected Error: {str(e)}"