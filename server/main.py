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
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database.database import Database
from services.WaiterService.waiter import WaiterAI

app = FastAPI()    

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

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

    response = waiter.prompt( user_prompt=request.prompt)
    return response

