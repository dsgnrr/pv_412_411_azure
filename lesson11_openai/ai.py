
import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

agent_model="gpt-5.4-mini"

deployment_name = "gpt-5.4-mini"

client = OpenAI(
    base_url=os.getenv("OPENAI_ENDPOINT"),
    api_key=os.getenv("OPENAI_KEY")
)

response = client.chat.completions.create(
    model=agent_model,
    messages=[
        {"role":"system", "content":"Ти senior C# розробник, вмієш створювати архітектурно-якісні веб-застосунки"},
        {"role":"user", "content":"Привіт розкажи будь-ласка, як мені побудувати простий форум і як мені його розгорнути на Azure App Service"}
    ]
)

print(response.choices[0].message.content)