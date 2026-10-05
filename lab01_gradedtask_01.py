# CSE325-2026-L01-K7QX-T1

RUN_PROFILE = "hand_written"


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    try:
        celsius = float(input("Celsius: "))
        print(f"{celsius}C = {celsius_to_fahrenheit(celsius)}F")
    except ValueError:
        print("Please enter a valid number.")
