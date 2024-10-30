import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('./waiterai.db')
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close_connection()

    def fetch_menu_items(self):
        menu_items = self.cursor.execute("SELECT * FROM menu_items")
        return menu_items.fetchall()
    
    def close_connection(self):
        self.connection.close()
    
    def create_manu_items(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS menu_items (
                                id INTEGER PRIMARY KEY,
                                name TEXT, price REAL,
                                description TEXT,
                                rating REAL,
                                image_url TEXT,
                                category TEXT
                            )
                            """)
        self.connection.commit()

        self.cursor.execute("""INSERT INTO menu_items (name, price, description, rating, image_url, category)
                            VALUES ('Hamburger', 5.99, 'A juicy hamburger', 4.5, 'https://www.example.com/hamburger.jpg', 'main')
                            """)
        
        self.connection.commit()