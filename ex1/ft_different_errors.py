def garden_operation(test_id: str) -> None:
    """A function that will generate errors
    according to the parameters given

    Args:
        test_id (str): key_word to generate a type of error
    """
    if (test_id == "ValueError" or test_id == "all"):
        int("abc")
    if (test_id == "ZeroDivisonError" or test_id == "all"):
        42 / 0
    if (test_id == "KeyError" or test_id == "all"):
        dico = {"Francois": "Holland", "Jean": "Castex",
                "Jean-Claude": "Van Damme"}
        dico["Nicolas"]
        # il est pas dans dico puisque il est en prison
    if (test_id == "FileNotFoundError" or test_id == "all"):
        open("Optifine.jar")


def test_error_types() -> None:
    """A function that will catch all different
    errors generted by the function garden_operation
    """
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        garden_operation("ValueError")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operation("ZeroDivisonError")
    except ZeroDivisionError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operation("FileNotFoundError")
    except FileNotFoundError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing KeyError...")
    try:
        garden_operation("KeyError")
    except KeyError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing multiple errors together...")
    try:
        garden_operation("all")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but the program continues !\n")

    print("All error types tested successfully !")


test_error_types()
