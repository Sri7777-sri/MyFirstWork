from database import IceCreamParlorDB
from utils import is_valid_seasonal_input, get_integer_input, get_string_input, display_flavor, display_cart_items


def main():
    db = IceCreamParlorDB()

    # Create tables if they don't exist already
    db.create_tables()

    while True:
        print("\n--- Icecream Parlor Management ---")
        print("1. Add Seasonal Flavor")
        print("2. Add Ingredient")
        print("3. Add Allergen")
        print("4. Search Flavors")
        print("5. Add To Cart")
        print("6. View Cart")
        print("7. Remove from Cart")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = get_string_input("Enter Flavor Name: ")
            description = get_string_input("Enter Description: ")
            while True:
                is_seasonal = input("Is Seasonal? (1-yes/0-no): ")
                if is_valid_seasonal_input(is_seasonal):
                    break
                print("Invalid input! Please enter 1 for seasonal or 0 for non-seasonal.")
            print(db.add_flavor(name, description, is_seasonal))

        elif choice == "2":
            name = get_string_input("Enter Ingredient Name: ")
            quantity = get_integer_input("Enter Quantity: ")
            unit = get_string_input("Enter Unit: ")
            print(db.add_ingredient(name, quantity, unit))

        elif choice == "3":
            name = get_string_input("Enter Allergen Name: ")
            print(db.add_allergen(name))

        elif choice == "4":
            keyword = get_string_input("Enter Keyword: ")
            results = db.search_flavors(keyword)
            if results:
                print("\nSearch Results:")
                for flavor in results:
                    display_flavor(flavor)
            else:
                print("\nNo Flavors found.")

        elif choice == "5":
            flavor_ID = get_integer_input("Enter Flavor ID to add to cart: ")
            print(db.add_to_cart(flavor_ID))

        elif choice == "6":
            items = db.view_cart()
            display_cart_items(items)

        elif choice == "7":
            flavor_ID = get_integer_input("Enter Flavor ID to remove from cart: ")
            print(db.remove_from_cart(flavor_ID))

        elif choice == "8":
            print("\nExiting...")
            break
        else:
            print("\nInvalid Choice, please try again.")


if __name__ == "__main__":
    main()
