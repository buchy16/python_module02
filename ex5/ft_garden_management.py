class GardenError(Exception):
    pass


class PlantNameError(GardenError):
    pass


class WaterLevelError(GardenError):
    pass


class SunlightHoursError(GardenError):
    pass


class Plant():
    def __init__(self, plant_name: str, water_level: int,
                 sunlight_hours: int) -> None:
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
    def __init__(self, tank_water_level):
        self.content = {}
        self.water_tank_level = tank_water_level

    @property
    def content(self) -> dict:
        return (self.__content)

    @content.setter
    def content(self, new_content: dict) -> dict:
        self.__content = new_content

    @property
    def water_tank_level(self) -> int:
        return (self.__water_tank_level)

    @water_tank_level.setter
    def water_tank_level(self, new_level) -> None:
        self.__water_tank_level = new_level

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
            if (self.content == {}):
                raise Exception("Error: Cannot water - no plant in the garden")
            plant: Plant
            for plant in self.content.values():
                print(f"Watering {plant.name} - success")
        except Exception as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    def checking_plant_health(self) -> None:
        try:
            plant: Plant
            for plant in self.content.values():
                if (plant.water_level > 10):
                    raise WaterLevelError(f"Error cheaking {plant.name}: \
Water level {plant.water_level} is too hight (max 10)\n")
                if (plant.water_level < 1):
                    raise WaterLevelError(f"Error cheaking {plant.name}: \
Water level {plant.water_level} is too hight (min 1)\n")
                if (plant.sunlight_hours > 12):
                    raise SunlightHoursError(f"Error cheaking {plant.name}: \
Sunlight hours {plant.sunlight_hours} is too hight (max 12)\n")
                if (plant.sunlight_hours < 2):
                    raise SunlightHoursError(f"Error cheaking {plant.name}: \
Sunlight hours {plant.sunlight_hours} is too hight (min 2)\n")
                print(f"{plant.name}: healthy (water: {plant.water_level}, \
sun: {plant.sunlight_hours})")
        except GardenError as e:
            print(e)

    def error_recovery(self):
        try:
            if (self.content == {}):
                raise Exception("Error: Cannot water - no plant in the garden")
            try:
                if (self.water_tank_level < 200):
                    raise WaterLevelError("Not enough water in tank")
            except WaterLevelError as e:
                print(f"Caught GardenError: {e}")
        except Exception as e:
            print(e)
        finally:
            print("System recovered and continuig...")


if (__name__ == "__main__"):
    garden1 = GardenManeger(100)
    garden2 = GardenManeger(100)

    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    garden1.add_plant(Plant("tomato", 5, 8))
    garden1.add_plant(Plant("lettuce", 15, 4))
    garden1.add_plant(Plant("", 5, 5))

    print("\nWatering plants...")
    garden1.water_plants()
    # garden2.water_plants()

    print("\nCheaking plant health...")
    garden1.checking_plant_health()

    print("\nTesting error recovery...")
    garden1.error_recovery()
    # garden2.error_recovery()

    print("\nGarden managment system test complete !")
