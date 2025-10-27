import pandas as pd
from tkinter import messagebox

"""Only allows float value to be entered."""
def validate_float(value: str):
    '''To allow only floats.'''
    if value == "":
        return True
    try:
        float(value)
        return True
    except ValueError:
        return False

"""Only allows integer value to be entered."""
def validate_int(value):
    if value == "" or value.isdigit():
        return True
    else:
        return False

"""Sorts the csv file in an ascending order."""
def file_sorter():
    df = pd.read_csv(filename)

    df = df.sort_values(by="Index", ascending=True)

    df.to_csv(filename, index=False)

"""Re-corrects the index column"""
def file_correcter():
    df = pd.read_csv(filename)

    values = df["Index"].values

    for i in range(len(values)):
        df.loc[i,"Index"] = i+1

    df.to_csv(filename, index=False)

"""Allows user to exit the current window."""
def destroyer(win):
    win.destroy()
    messagebox.showinfo("Success","Successfully exited..")

