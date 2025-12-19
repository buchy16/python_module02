class GardenError(Exception):
    """A garden Exception class for error on the
    garden

    Args:
        Exception (class): Original class use with try
        and except
    """
    pass


class PlantNameError(GardenError):
    """A plant name Exeception class for error on
    the name of plant, it inherits from GardenError

    Args:
        GardenError (class): the general exception class for plant
    """
    pass


class WaterLevelError(GardenError):
    """A plant water level Exeception class for error on
    the water level of plant, it inherits from GardenError

    Args:
        GardenError (class): the general exception class for plant
    """
    pass


class SunlightHoursError(GardenError):
    """A plant sunlight hours Exeception class for error on
    the sunlight hours of plant, it inherits from GardenError

    Args:
        GardenError (class): the general exception class for plant
    """
    pass


class Plant():
    """The classic class plant, secured with the use of property
    """
    def __init__(self, plant_name: str, water_level: int,
                 sunlight_hours: int) -> None:
        """Initializes a new Plant object

        Args:
            plant_name (str): plant name
            water_level (int): water level of the plant
            sunlight_hours (int): level of sunlight hours
        """
        self.name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

    @property
    def name(self) -> str:
        """creat a new proprty named name

        Returns:
            str: plant name
        """
        return (self.__name)

    @name.setter
    def name(self, new_name: str) -> None:
        """Operator Overloading for the property name
        set the name of plant to 'new_name'

        Args:
            new_name (str): new name to attribute to the plant
        """
        self.__name = new_name

    @property
    def water_level(self) -> int:
        """creat a new property named water_level

        Returns:
            int: the water level of the plant
        """
        return (self.__water_level)

    @water_level.setter
    def water_level(self, level: int) -> None:
        """Operator Overloading for the property water_level
        set the name of plant to 'level'

        Args:
            level (int): new level to attribute to the plant
        """
        self.__water_level = level

    @property
    def sunlight_hours(self) -> int:
        """creat a new property named sunlight_hours

        Returns:
            int: sunlight hours
        """
        return (self.__sunlight_hours)

    @sunlight_hours.setter
    def sunlight_hours(self, hours: int) -> None:
        """Operator Overloading for the property sunlight_hours
        set the name of plant to 'hours'

        Args:
            hours (int): hours to attribute to the plant
        """
        self.__sunlight_hours = hours


class GardenManeger():
    """A class to operate safely on multiple plants
    """
    def __init__(self, tank_water_level: int):
        """Initializes a new garden object
        this object use a dictionary to store all the plants

        Args:
            tank_water_level (int): water level on the garden tank
        """
        self.content = {}
        self.water_tank_level = tank_water_level

    @property
    def content(self) -> dict:
        """creat a new property namd content

        Returns:
            dict: dictionary with all the plant
        """
        return (self.__content)

    @content.setter
    def content(self, new_content: dict) -> None:
        """Operator Overloading for the property content
        set the name of plant to 'new_content'

        Args:
            new_content (dict): new dictionary to atrribut to garden
        """
        self.__content = new_content

    @property
    def water_tank_level(self) -> int:
        """creat a new attribut named water_tank_level

        Returns:
            int: water level of the garden tank
        """
        return (self.__water_tank_level)

    @water_tank_level.setter
    def water_tank_level(self, new_level: int) -> None:
        """Operator Overloading for the property content
        set the name of plant to 'new_content'

        Args:
            new_level (int): new water level to attribut to the garden tank
        """
        self.__water_tank_level = new_level

    def add_plant(self, plant: Plant) -> None:
        """A method tha add the given plant to the content of the garden
        If the name of the plant is invalid, an error will be display but
        the programme will continues

        Args:
            plant (Plant): A plant object to add in the garden content

        """
        try:
            if (plant.name == "" or (not isinstance(plant.name, str))):
                raise PlantNameError("Error adding plant: Plant name \
cannot be empty !")
            print(f"Added {plant.name} successfully")
            self.content[plant.name] = plant
        except GardenError as e:
            print(e)

    def water_plants(self) -> None:
        """A method that will automatically water all plant on the garden
        if there are no plant on the garden, an error will be display and the
        water systeme will close

        """
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
        """A methode that will cheack all plant on the content to see
        if they are in good health, if not, the probleme with details will
        be display

        """
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
        """A method that will check for error on the garden systeme
        if an error is found, the programme will try to fix it
        (bye adding water in the tank for exemple)

        """
        try:
            if (self.content == {}):
                raise GardenError("No plant in the garden")
            try:
                if (self.water_tank_level < 200):
                    raise WaterLevelError("Not enough water in tank")
                print("Systeme is operationel")
            except WaterLevelError as e:
                print(f"Caught GardenError: {e}")
                self.water_tank_level += 100
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("System recovered and continuig...")


# if (__name__ == "__main__"):
#     garden1 = GardenManeger(100)
#     garden2 = GardenManeger(100)

#     print("=== Garden Management System ===\n")

#     print("Adding plants to garden...")
#     garden1.add_plant(Plant("tomato", 5, 8))
#     garden1.add_plant(Plant("lettuce", 15, 4))
#     garden1.add_plant(Plant("", 5, 5))

#     print("\nWatering plants...")
#     garden1.water_plants()
#     # garden2.water_plants()

#     print("\nCheaking plant health...")
#     garden1.checking_plant_health()

#     print("\nTesting error recovery...")
#     garden1.error_recovery()
#     # garden1.error_recovery()
#     # garden2.error_recovery()

#     print("\nGarden managment system test complete !")
