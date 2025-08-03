def convert_temperature(temp, unit):
    if unit.upper() == 'F':
        converted = (temp - 32) * 5/9
        return round(converted, 2)
    elif unit.upper() == 'C':
        converted = (temp * 9/5) + 32
        return round(converted, 2)
    else:
        return "Invalid unit. Use 'F' or 'C'."

if __name__ == "__main__":
    try:
        temperature = float(input("Enter the temperature: "))
        unit = input("Enter the unit ('F' or 'C'): ")
        result = convert_temperature(temperature, unit)
        print("Converted Temperature:", result)
    except ValueError:
        print("Invalid input. Please enter a number.")
