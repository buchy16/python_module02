def check_temperature(temp_str: str) -> None:
    """A function that will try to convert temp_str
    into a integer, of the temp_str can't be converted
    an error will bw returned (but the programme will not stop)
    if the number converted is greather than 40, an error will be display
    if the number is smaller than 0, an error will be display

    Args:
        temp_str (str): a string number
    """
    print(f"Testing temperature: {temp_str}")
    try:
        temp_int = int(temp_str)
        if (temp_int >= 0 and temp_int <= 40):
            print(f"Temperature {temp_int}°C is perfect for plants !")
        else:
            if (temp_int < 0):
                print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
            else:
                print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    print("All tests completed - program didn't crash !")
