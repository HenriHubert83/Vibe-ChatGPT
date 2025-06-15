import random

def generate_four_digit_number():
    """Return a random four-digit string from 0000 to 9999."""
    return f"{random.randint(0, 9999):04d}"

if __name__ == "__main__":
    print(generate_four_digit_number())
