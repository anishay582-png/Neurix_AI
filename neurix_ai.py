
import os
from dotenv import load_dotenv
from openai import OpenAI


# Load API key from .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "API key not found. Please check your .env file."
    )


# Connect to OpenAI
client = OpenAI(api_key=api_key)


# Chatbot configuration
BOT_NAME = "Nova AI"

MODEL_NAME = "gpt-4.1-mini"


# AI personality and instructions
SYSTEM_PROMPT = """
You are Nova AI, a friendly and intelligent AI assistant.

Your job is to:
1. Answer questions clearly and accurately.
2. Explain difficult topics in simple English.
3. Help with Python programming.
4. Help with AI and machine learning.
5. Assist with general knowledge.
6. Give step-by-step explanations when requested.
7. Be polite, helpful and professional.
8. Admit when you do not know something.
9. Never invent facts intentionally.

Keep your answers useful and easy to understand.
"""


# Conversation memory
conversation = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


def get_ai_response(user_message):

    # Add user question
    conversation.append({
        "role": "user",
        "content": user_message
    })

    try:

        # Send conversation to AI
        response = client.responses.create(
            model=MODEL_NAME,
            input=conversation
        )

        # Extract AI answer
        answer = response.output_text

        # Save AI answer in conversation history
        conversation.append({
            "role": "assistant",
            "content": answer
        })

        return answer

    except Exception as error:

        # Remove unanswered user message
        conversation.pop()

        print("\nError connecting to AI:", error)

        return (
            "Sorry, I could not connect to the AI. "
            "Please check your internet connection, "
            "API key and API billing."
        )


def start_chatbot():

    print("=" * 50)
    print("          WELCOME TO NOVA AI")
    print("          Your Smart AI Assistant")
    print("=" * 50)

    print("Ask me anything!")
    print("Type 'bye' to exit.\n")

    while True:

        user_message = input("You: ").strip()

        if not user_message:
            continue

        if user_message.lower() in [
            "bye",
            "exit",
            "quit"
        ]:

            print(
                f"\n{BOT_NAME}: Goodbye! "
                "Have a wonderful day."
            )

            break

        print(f"\n{BOT_NAME}: ", end="", flush=True)

        answer = get_ai_response(user_message)

        print(answer)
        print()


# Run chatbot
if __name__ == "__main__":
    start_chatbot()
