import sqlite3

class IceCreamParlorDB:
    def __init__(self):
        self.db_name = "ice_cream_parlor.db"

    def connect(self):
        """Create a connection to the SQLite database."""
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        """Create all necessary tables if they don't exist."""
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS flavors (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                is_seasonal INTEGER
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ingredients (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                quantity INTEGER,
                unit TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS allergens (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cart (
                id INTEGER PRIMARY KEY,
                flavor_id INTEGER,
                FOREIGN KEY (flavor_id) REFERENCES flavors (id)
            )
        """)

        connection.commit()
        connection.close()

    def insert_flavors(self):
        """Insert some default flavors into the 'flavors' table."""
        flavors_to_add = [
            ("Vanilla Bliss", "Classic vanilla with rich cream", 0),
            ("Chocolate Burst", "Dark chocolate with nuts", 0),
            ("Pistachio Perfection", "A balanced flavor of pistachios", 0),
            ("Butterscotch Delight", "Rich butterscotch with a satisfying flavor", 1),
            ("Mango Mirage", "An exotic, dream-like mango experience", 1)
        ]

        connection = self.connect()
        cursor = connection.cursor()
        cursor.executemany("""
            INSERT INTO flavors (name, description, is_seasonal)
            VALUES (?, ?, ?)
        """, flavors_to_add)

        connection.commit()
        connection.close()

    def insert_ingredients(self):
        """Insert some default ingredients into the 'ingredients' table."""
        ingredients_to_add = [
            ("Milk", 100, "Liters"),
            ("Sugar", 50, "Kg"),
            ("Chocolate Chips", 30, "Kg"),
            ("Nuts", 20, "Kg"),
            ("Vanilla Extract", 5, "Liters")
        ]

        connection = self.connect()
        cursor = connection.cursor()
        cursor.executemany("""
            INSERT INTO ingredients (name, quantity, unit)
            VALUES (?, ?, ?)
        """, ingredients_to_add)

        connection.commit()
        connection.close()

    def insert_allergens(self):
        """Insert some default allergens into the 'allergens' table."""
        allergens_to_add = [
            ("Nuts"),
            ("Milk"),
            ("Chocolate"),
            ("Soy")
        ]

        connection = self.connect()
        cursor = connection.cursor()
        cursor.executemany("""
            INSERT INTO allergens (name)
            VALUES (?)
        """, [(allergen,) for allergen in allergens_to_add])

        connection.commit()
        connection.close()

    def insert_suggestions(self):
        """Insert some sample suggestions into the 'suggestions' table."""
        suggestions_to_add = [
            ("Add more seasonal flavors!", 1),
            ("Consider lactose-free options.", 0)
        ]

        connection = self.connect()
        cursor = connection.cursor()
        cursor.executemany("""
            INSERT INTO suggestions (message, flavor_id)
            VALUES (?, ?)
        """, suggestions_to_add)

        connection.commit()
        connection.close()

    # Flavor management
    def add_flavor(self, name, description, is_seasonal):
        """Add a new flavor to the 'flavors' table."""
        connection = self.connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO flavors (name, description, is_seasonal)
                VALUES (?, ?, ?)
            """, (name, description, is_seasonal))
            connection.commit()
        except sqlite3.IntegrityError:
            return f"Flavor '{name}' already exists!"
        finally:
            connection.close()
        return f"Flavor '{name}' added successfully!"

    def search_flavors(self, keyword):
        """Search for flavors based on a keyword."""
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, name, description, is_seasonal 
            FROM flavors WHERE name LIKE ?
        """, (f"%{keyword}%",))
        results = cursor.fetchall()
        connection.close()
        return results

    # Cart operations
    def add_to_cart(self, flavor_id):
        """Add a flavor to the cart."""
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO cart (flavor_id)
            VALUES (?)
        """, (flavor_id,))
        connection.commit()
        connection.close()
        return f"Flavor ID '{flavor_id}' added to cart!"

    def view_cart(self):
        """View all items currently in the cart."""
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT flavors.id, flavors.name 
            FROM cart 
            INNER JOIN flavors ON cart.flavor_id = flavors.id
        """)
        items = cursor.fetchall()
        connection.close()
        return items

    def remove_from_cart(self, flavor_id):
        """Remove a flavor from the cart."""
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
            DELETE FROM cart WHERE flavor_id = ?
        """, (flavor_id,))
        connection.commit()
        connection.close()
        return f"Flavor ID '{flavor_id}' removed from cart!"


    # Ingredient management
    def add_ingredient(self, name, quantity, unit):
        """Add a new ingredient to the 'ingredients' table."""
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO ingredients (name, quantity, unit)
            VALUES (?, ?, ?)
        """, (name, quantity, unit))
        connection.commit()
        connection.close()
        return f"Ingredient '{name}' added successfully!"

    # Allergen management
    def add_allergen(self, name):
        """Add a new allergen to the 'allergens' table."""
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO allergens (name)
            VALUES (?)
        """, (name,))
        connection.commit()
        connection.close()
        return f"Allergen '{name}' added successfully!"
