import argparse
import os

import openai
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# Create a new chat session
def create_chat_session(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.7,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    # Set up command line arguments
    parser = argparse.ArgumentParser(
        description="Start a new chat session with OpenAI GPT-3"
    )
    parser.add_argument(
        "--prompt", required=True, help="The prompt to start the chat session"
    )

    # Parse command line arguments
    args = parser.parse_args()

    # Create a new chat session
    response = create_chat_session(args.prompt)

    # Print the chat session response
    print(response)
