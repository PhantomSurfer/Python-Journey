def fahrenheit_to_celsius():
    while True:
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))

            # Check if temperature is above absolute zero
            if fahrenheit < -459.67:
                raise ValueError("Temperature should be greater than absolute zero.")

            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
            break

        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

fahrenheit_to_celsius()
