def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """A function that will check if all the parameters
    given are correct, if that's the case a message saying
    that the plant is healthy will be display

    Args:
        plant_name (str): plant name
        water_level (int): water level of the plant
        sunlight_hours (int): sunlight hours of the plant
    """
    try:
        if (not isinstance(plant_name, str) or plant_name == ""):
            raise ValueError("Error: Plant name cannot be empty\n")

        try:
            if (water_level > 10):
                raise ValueError(f"Error: Water level {water_level} is too \
hight (max 10)\n")
            if (water_level < 1):
                raise ValueError(f"Error: Water level {water_level} is too \
low (min 10)\n")
            try:
                if (sunlight_hours > 12):
                    raise ValueError(f"Error: Sunlight hours {sunlight_hours} \
is too hight (max 12)\n")
                if (sunlight_hours < 2):
                    raise ValueError(f"Error: Sunlight hours {sunlight_hours} \
is too low (min 2)\n")
                print(f"Plant '{plant_name}' is healthy !\n")
            except ValueError as e:
                print(e)

        except ValueError as e:
            print(e)
    except ValueError as e:
        print(e)


def test_plant_checks() -> None:
    """A function to test the function check_plant_health
    with good and bad values
    """
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    check_plant_health("tomato", 8, 8)

    print("Testing empty plant name...")
    check_plant_health("", 8, 8)

    print("Testing bad water level...")
    check_plant_health("tomato", 150, 8)

    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 8, 10000)

    print("All error raising tests completed !")


# test_plant_checks()
