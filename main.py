from flask import Flask
from utils import Utils

def main() -> None:
    print(Utils(farenheit=49).temperature_converter_to_Celsius())

if __name__ == '__main__':
    main()