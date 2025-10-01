italian_food = [
    "Pasta Bolognese",
    "Pepperoni pizza",
    "Margherita pizza",
    "Lasagna"
]

indian_food = [
    "Curry",
    "Chutney",
    "Samosa",
    "Naan"
]

def find_meal(name, menu):
    return name if name in menu else None

def select_meal(name, food_type):
    food_type = food_type.capitalize()  # Normalizar entrada
    if food_type == "Italian":
        print("Available Italian Meals:")
        for meal in italian_food:
            print(meal)
        return find_meal(name, italian_food)
    elif food_type == "Indian":
        print("Available Indian Meals:")
        for meal in indian_food:
            print(meal)
        return find_meal(name, indian_food)
    else:
        print("Invalid food type")
        return None

def display_available_meals(food_type):
    food_type = food_type.capitalize()  # Normalizar entrada
    if food_type == "Italian":
        print("Available Italian Meals:")
        for meal in italian_food:
            print(meal)
    elif food_type == "Indian":
        print("Available Indian Meals:")
        for meal in indian_food:
            print(meal)
    else:
        print("Invalid food type")

def create_summary(name, amount, food_type):
    order = select_meal(name, food_type)
    if order:
        return f"You ordered {amount} {name}"
    else:
        return "Meal not found"

print("Welcome to the Food Order System!")

# Pedir tipo de comida y validar
while True:
    type_input = input("Enter the type of food you want to order (Italian/Indian): ").capitalize()
    if type_input in ["Italian", "Indian"]:
        break
    print("Please enter a valid food type (Italian or Indian).")

# Mostrar comidas disponibles
display_available_meals(type_input)

# Pedir nombre de la comida
name_input = input("Enter the name of the meal you want to order: ")

# Pedir cantidad con manejo de errores
while True:
    try:
        amount_input = int(input("Enter the quantity you want to order: "))
        if amount_input > 0:
            break
        print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid number.")

result = create_summary(name_input, amount_input, type_input)
print(result)