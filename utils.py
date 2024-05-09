class Utils:
    def __repr__(self) -> str:
        "All possible util functions are defined here"

    def __init__(self, farenheit) -> None:
        self.farenheit = farenheit

    def temperature_converter_to_Celsius(self) -> float:
        return round((self.farenheit - 32) * 5.0/9.0, 2)