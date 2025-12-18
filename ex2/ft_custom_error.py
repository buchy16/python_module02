class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def garden_operation(test_id: str) -> None:
    """A function that will generate errors
    according to the parameters given

    Args:
        test_id (str): key_word to generate a type of error
    """
    if (test_id == "PlantError" or test_id == "all"):
        tomato = ["tomato", "is_wiling"]
        if (tomato[1] == "is_wiling"):
            raise PlantError(f"The {tomato[0]} plant is wiling !")

    if (test_id == "WaterError" or test_id == "all"):
        tank = 100
        if (tank < 500):
            raise WaterError("Not enought water in the tank !")


def custom_error() -> None:
    """A function that will catch all different
    errors generted by the function garden_operation
    """
    print("=== Garden Error Types Demo ===\n")
    print("Testing PlantError...")
    try:
        garden_operation("PlantError")
    except GardenError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operation("WaterError")
    except GardenError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all errors...")
    try:
        garden_operation("PlantError")
    except (GardenError) as e:
        print(f"Caught a garden error: {e}")
    try:
        garden_operation("WaterError")
    except (GardenError) as e:
        print(f"Caught a garden error: {e}\n")

    print("All custom error types work correctly !")


# custom_error()
