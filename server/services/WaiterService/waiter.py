import anthropic
import os
from dotenv import load_dotenv
from database.database import Database


load_dotenv()

class WaiterAI:
    def __init__(self):
        self.client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

    # TODO: Add prompt types for different types of prompts (orders, questions, etc.)
    def prompt(self, user_prompt):
        system_prompt = self.build_system_prompt()

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

        return message.content[0].text

    def take_order_prompt(self, order):
        pass

    def send_order_to_kitchen(self, order):
        pass

    def build_system_prompt(self):
        with Database() as db:
            menu_items = db.fetch_menu_items()

        systemPrompt = f"""You are a professional and charismatic waiter at a restaurant that prides itself on its excellent customer service. Your job is to help customers with their inquiries regarding the restaurant, the menu or to connect them with the correct human assistance. 

        Here is the restaurant menu:\n\n

        {menu_items} \n\n

        Here are some details about the restaurant:

        Restaurant is named MamaBistro. We have been opened since 1954  and have locations in Vancouver, Toronto, and Ottawa. It is a family owned restaurant focusing on bringing the best north American cuisine. 
        
        Please do not make up or guess any unknown information. If you do not know the answer, please say so and ask the customer if they would like to speak to a human waiter or manager.
        """
        
        return systemPrompt