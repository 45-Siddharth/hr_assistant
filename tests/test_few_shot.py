from services.openai_service import client

from core.config import (
    AZURE_OPENAI_DEPLOYMENT
)

from services.context_service import (
    load_context
)

from prompts.few_shot_prompt_builder import (
    build_few_shot_prompt
)



question = """

How many sick leaves do employees receive?

"""


context = load_context()



prompt = build_few_shot_prompt(
    context,
    question
)



response = client.chat.completions.create(

    model=AZURE_OPENAI_DEPLOYMENT,

    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ],

    temperature=0.2,

    max_completion_tokens=300
)



print(
    response.choices[0]
    .message.content
)