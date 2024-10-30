import openai
import os 
from dotenv import load_dotenv

load_dotenv()

# set your API key

openai.api_key = os.getenv("YOUR_OPENAI_API_KEY")


# Function to send a question to GPT-4
def pergunte_ao_chatgpt(pergunta:str):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            ("roles": "user", "content": pergunta)
        ]
    )
    # Extracting the actual content message from the response
    return response.choices[0].message.content

# Asking the question
question = "A minha empresa está lucrando quanto nesse mês?"
answer = pergunte_ao_chatgpt(question)

# Print the response
print(f"Resposta do ChatGPT: {answer}")
