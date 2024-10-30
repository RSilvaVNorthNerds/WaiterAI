import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

class WaiterAI:
    def __init__(self):
        self.client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

    # TODO: Add prompt types for different types of prompts (orders, questions, etc.)
    def prompt(self, system_prompt, user_prompt):
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            temperature=0,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user_prompt
                        }
                    ]
                }
            ]
        )

        return {"content": message}

    def take_order_prompt(self, order):
        pass

    def send_order_to_kitchen(self, order):
        pass