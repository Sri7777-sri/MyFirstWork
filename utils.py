def is_valid_seasonal_input(seasonal_input):
    """
    Validates if the input for seasonal flavor is either 1 (yes) or 0 (no).
    """
    if seasonal_input not in ['0','1']:
        return False
    return True

def get_integer_input(prompt, min_value=None, max_value=None):
    """
    Prompts the user for integer input, ensuring it falls within an optional range.
    """
    while True:
        try:
            user_input = int(input(prompt))
            if (min_value is not None and user_input < min_value) or (max_value is not None and user_input > max_value):
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return user_input
        except ValueError:
            print("Invalid input! Please enter an integer.")

def get_string_input(prompt):
    """
    Prompts the user for a string input, and ensures the input is not empty.
    """
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input
        print("Input cannot be empty. Please try again.")

def display_flavor(flavor):
    """
    Helper function to display a single flavor's details in a formatted way.
    """
    seasonal_status = "Yes" if flavor[3] == 1 else "No"
    print(f"ID: {flavor[0]}, Name: {flavor[1]}, Description: {flavor[2]}, Seasonal: {seasonal_status}")

def display_cart_items(cart_items):
    """
    Displays all items in the cart in a user-friendly format.
    """
    if cart_items:
        print("\nCart items:")
        for item in cart_items:
            print(f"ID: {item[0]}, Name: {item[1]}")
    else:
        print("\nCart is empty!")
