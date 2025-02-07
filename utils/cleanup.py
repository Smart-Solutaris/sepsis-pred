import pandas as pd
import os
import pathlib


def dataset1(path:str) -> pd.DataFrame:
    data = pd.DataFrame()
    #read through the folder
    count = 0;
    #trainingsetA = pd.concat(trainingsetA, pd)
    for f in pathlib.Path(path).iterdir():
        print(f)
        count+= 1
        df = pd.read_csv(f, sep="|")
        data = pd.concat([data, df], ignore_index=True)

    return data


if __name__ == "__main__":
    base_url = "../dataset/training_setA"

    dataset1(path=base_url)