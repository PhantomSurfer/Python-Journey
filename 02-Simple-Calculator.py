def calculator():
    while True:
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")

        choice = int(input("Enter choice(1/2/3/4/5): "))
        print("")

        if choice == 5:
            print("Exiting calculator...")
            break

        num1 = float(input("Enter first number: "))
        print("")
        num2 = float(input("Enter second number: "))
        print("")

        if choice == 1:
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
            print("")

        elif choice == 2:
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
            print("")

        elif choice == 3:
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
            print("")

        elif choice == 4:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
            print("")

        else:
            print("Invalid choice. Please select a valid operation.")
            print("")

calculator()
