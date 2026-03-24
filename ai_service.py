import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load environment variables from .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def create_simple_task(description):
    if not client.api_key:
        raise ValueError(
            "OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

    try:
        prompt = f"""Please split the following task into smaller, manageable subtasks:\n\n{description}\n\nSubtasks:
        Task: {description}
        
        Response format:
        - Subtask 1
        - Subtask 2
        - Subtask 3
        - ...
        Return only with the subtasks in a list format with a bullet icon per line.
        """

        params = {
            "model": "gpt-5",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant that breaks down tasks into smaller subtasks."},
                {"role": "user", "content": prompt}],
            "reasoning_effort": "minimal",
            "max_completion_tokens": 300,
            "verbosity": "medium"
        }

        response = client.chat.completions.create(**params)
        subtasks = response.choices[0].message.content.strip().split("\n")
        return [subtask.strip("- ").strip() for subtask in subtasks if subtask.strip()]

    except Exception as e:
        print(f"An error occurred while creating the task: {e}")
