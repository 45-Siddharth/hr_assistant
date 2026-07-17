from openai import AzureOpenAI
from core.config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_VERSION
)
# Initialize the client with the correct Azure AI Project API version
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint= AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION 
)

response = client.chat.completions.create(
    model=AZURE_FINETUNE_MODEL,  # Ensure this matches your exact DEPLOYMENT name in Azure
    messages=[
        {
            "role": "system",
            "content": "You are Vaayu Enterprise HR Assistant. Answer employee HR questions professionally using company policies only."
        },
        {
            "role": "user",
            "content": "who is prakhar dubey??"
        }
    ],
    temperature=0.2
)

print(response.choices[0].message.content)