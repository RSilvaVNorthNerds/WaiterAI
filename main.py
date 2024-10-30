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
from database.database import Database

app = FastAPI()

@app.get("/")
def read_root():
    with Database() as db:
        menu_items = db.fetch_menu_items()
    return {"items": menu_items}
