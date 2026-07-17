from services.openai_service import client

from core.config import (
    AZURE_OPENAI_DEPLOYMENT
)

from services.context_service import (
    load_context
)

from prompts.context_prompt import (
    build_prompt
)


context = get_relevant_context(question)


question = """
How many annual leaves do employees receive?
"""


final_prompt = build_prompt(
    context,
    question
)


response = client.chat.completions.create(

    model=AZURE_OPENAI_DEPLOYMENT,

    messages=[

        {
            "role":"user",
            "content":final_prompt
        }

    ],

    temperature=0.2,

    max_completion_tokens=300
)


print(
    response.choices[0]
    .message.content
)