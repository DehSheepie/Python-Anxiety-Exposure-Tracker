from os import path

filename = "data.csv"

def check_file_exists():
    if not path.exists(filename):
        file = open(filename, "w")


def read_from_file():
    if path.exists(filename):
        with open(filename, "r") as file:
            data = file.read().splitlines()
            return data
    return []


def write_to_file(data: [str]):
    with open(filename, "w") as file:
        for element in data:
            file.write(f"{element.lower()}\n")

