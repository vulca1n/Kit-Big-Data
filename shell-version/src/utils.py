"""Utility functions."""

import json
from pathlib import Path


def read_json(filename: str) -> dict:
    """
    Read data from a JSON file.

    :param filename: The name of the JSON file to read.
    :type filename: str
    :return: The data read from the JSON file,
        represented as a dictionary.
    :rtype: dict
    """
    if not Path("src/data/").exists():
        Path.mkdir("src/data/")
    if not Path("src/data/tasks.json").exists():
        Path.touch("src/data/tasks.json")
        data = {}
        write_json("src/data/tasks.json", data)
    with open(filename, "r+", encoding="utf-8") as file:
        data = json.load(file)
    return data


def write_json(filename: str, data: dict):
    """
    Write data to a JSON file.

    :param filename: The name of the JSON file to write to.
    :type filename: str
    :param data: The data to be written to the JSON file,
        represented as a dictionary.
    :type data: dict
    """
    with open(filename, "w+", encoding="utf-8") as file:
        json.dump(data, file)
