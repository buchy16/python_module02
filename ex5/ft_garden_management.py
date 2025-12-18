class GardenError(Exception):
    pass


class PlantNameError(GardenError):
    pass


class WaterLevelError(GardenError):
    pass


class SunlightHoursError(GardenError):
    pass


class Plant():
    def __init__(self, plant_name: str, water_level: int, sunlight_hours: int) -> None:
        self.name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

    @property
    def name(self) -> str:
        return (self.__name)

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

    @property
    def water_level(self) -> int:
        return (self.__water_level)

    @water_level.setter
    def water_level(self, level) -> None:
        self.__water_level = level

    @property
    def sunlight_hours(self) -> int:
        return (self.__sunlight_hours)

    @sunlight_hours.setter
    def sunlight_hours(self, hours) -> None:
        self.__sunlight_hours = hours


class GardenManeger():
    def __init__(self):
        self.content = {}

    @property
    def content(self) -> dict:
        return (self.__content)

    @content.setter
    def content(self, new_content: dict) -> dict:
        self.__content = new_content

    def add_plant(self, plant: Plant) -> None:
        try:
            if (plant.name == "" or (not isinstance(plant.name, str))):
                raise PlantNameError("Error adding plant: Plant name \
cannot be empty !")
            print(f"Added {plant.name} successfully")
            self.content[plant.name] = plant
        except GardenError as e:
            print(e)

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            plant: Plant
            for plant in self.content.values():
                plant.name + "42"
                print(f"Watering {plant}")

        except TypeError:
            print(f"Error: Cannot water {plant} - invalide plant")
        finally:
            print("Closing watering system (cleanup)")


if (__name__ == "__main__"):
    garden1 = GardenManeger()

    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    garden1.add_plant(Plant("tomato", 5, 8))
    garden1.add_plant(Plant("lettuce", 15, 4))
    garden1.add_plant(Plant("", 5, 5))

    print("\nWatering plants...")
    garden1.water_plants()

