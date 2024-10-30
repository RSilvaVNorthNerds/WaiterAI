import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('./waiterai.db')
        self.connection.row_factory = sqlite3.Row
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
    
    def create_menu_items(self):
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
                            VALUES ('Hamburger', 5.99, 'A juicy hamburger', 4.5, 'https://www.example.com/hamburger.jpg', 'main'),
                            ('Fries', 2.99, 'Crispy fries', 4.0, 'https://www.example.com/fries.jpg', 'side'),
                            ('Coke', 1.99, 'A refreshing coke', 4.0, 'https://www.example.com/coke.jpg', 'drink'),
                            ('Salad', 3.99, 'A fresh salad', 4.0, 'https://www.example.com/salad.jpg', 'main'),
                            ('Ice Cream', 2.99, 'A sweet ice cream', 4.0, 'https://www.example.com/ice_cream.jpg', 'dessert'),
                            ('Water', 0.99, 'A refreshing water', 4.0, 'https://www.example.com/water.jpg', 'drink'),
                            ('Pizza', 7.99, 'A delicious pizza', 4.0, 'https://www.example.com/pizza.jpg', 'main'),
                            ('Pasta', 6.99, 'A tasty pasta', 4.0, 'https://www.example.com/pasta.jpg', 'main'),
                            ('Soup', 4.99, 'A warm soup', 4.0, 'https://www.example.com/soup.jpg', 'main'),
                            ('Bread', 1.99, 'A fresh bread', 4.0, 'https://www.example.com/bread.jpg', 'side'),
                            ('Cake', 3.99, 'A sweet cake', 4.0, 'https://www.example.com/cake.jpg', 'dessert')
                            """)
        
        self.connection.commit()