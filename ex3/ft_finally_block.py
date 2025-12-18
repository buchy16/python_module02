def water_plants(plant_list: list) -> None:
    """A funstion that will test if the name of the plant
    is valide and thene water all plant in the list
    if a plant name is not valid a custom error message will be display
    and the watering systeme will close

    Args:
        plant_list (list): a list of plants to water
    """
    print("Opening watering system")
    try:
        plant: str
        for plant in plant_list:
            plant + "42"
            print(f"Watering {plant}")

    except TypeError:
        print(f"Error: Cannot water {plant} - invalide plant")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """A function to test the water_plant function
    with good and bad values
    """
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots", "radish"])
    print("Watering completed successfully !")

    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots", "radish"])
    print("\nCleanup always happens, even with errors !")


test_watering_system()
