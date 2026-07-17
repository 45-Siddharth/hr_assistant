from services.openai_service import client

from core.config import AZURE_OPENAI_DEPLOYMENT

from prompts.prompt_template import load_prompt



system_prompt = load_prompt()


user_question = """
How many vacation days do employees receive?
"""


response = client.chat.completions.create(

    model=AZURE_OPENAI_DEPLOYMENT,

    messages=[

        {
            "role":"system",
            "content":system_prompt
        },

        {
            "role":"user",
            "content":user_question
        }

    ],

    temperature=0.2,

    max_completion_tokens=300

)


print(
    response.choices[0]
    .message.content
)