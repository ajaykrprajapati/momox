"""
    Entry point for momox app.

    File name: main.py
    Author: Ajay Prajapati
    Date created: 17/07/2021
    Date last modified: 17/07/2021
    Python Version: 3.8.2
    Version: 1.0.1
"""


# import logging
import os

from .utils.csv_utils import process_data, read_csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, "static/abc.csv")

print(filepath)


def main_func():
    df = read_csv(filepath)
    print("head", df.head)
    process_data(df)
