"""
WaiterAI 

Features:
- Interperate inputted menu
- Take orders from customers
- Send orders to the kitchen
- Send notifications to customers when their order or table is ready

Services:
- Waiter Service 
- Orders Service
- Notification Service


"""

from fastapi import FastAPI
from pydantic import BaseModel
from database.database import Database
from services.WaiterService.waiter import WaiterAI

app = FastAPI()    

@app.get("/fetch_menu_items")
def read_root():
    with Database() as db:
        menu_items = db.fetch_menu_items()
    return {"items": menu_items}

class WaiterRequest(BaseModel):
    prompt: str

@app.post("/submit_waiter_request")
def submit_waiter_request(request: WaiterRequest):
    waiter = WaiterAI()

    systemPrompt = """You are a professional and charismatic waiter at a restaurant that prides itself on its excellent customer service. Your job is to help customers with their inquiries regarding the restaurant, the menu or to connect them with the correct human assistance. 

    Here is the restaurant menu:

    Hamburger - $5.99, 4/5 rating, Juicy beef hamburger
    Soda - $5.99, 4/5 rating, Juicy beef hamburger
    Salad - $5.99, 4/5 rating, Juicy beef hamburger

    Here are some details about the restaurant:

    Restaurant is named MamaBistro. We have been opened since 1954  and have locations in Vancouver, Toronto, and Ottawa. It is a family owned restaurant focusing on bringing the best north American cuisine. 
    
    Please do not make up or guess any unknown information. If you do not know the answer, please say so and ask the customer if they would like to speak to a human waitor or manager.
    """

    response = waiter.prompt(system_prompt=systemPrompt, user_prompt=request.prompt)
    return response

