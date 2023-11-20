user_input = input("How many kilometers did you run today?")

def convert_to_miles(km):
    user_input_as_float = float(user_input)
    converted_answer = round(user_input_as_float / 1.60934, 2)
    return converted_answer

print(f"Your {user_input}km run was {convert_to_miles(user_input)}mi")
