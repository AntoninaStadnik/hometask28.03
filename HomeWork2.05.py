# Напишіть програму для збереження даних про музичні
# групи у вигляді словника, де ключ – назва групи, значення –
# список альбомів.
# Напишіть функціонал:
#  додати новий гурт
#  додати новий альбом
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle

import json
import pickle


def load_data_json(filename: str = "music.json") -> dict[str, list[str]]:
    with open(filename, 'r', encoding= "utf-8") as file:
         data = json.load(file)
    return data

def save_data_json(data: dict[str, list[str]], filename: str = "music.json") -> None:
    with open(filename, 'w', encoding= "utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def save_data_pickle(data: dict[str, list[str]], filename: str = "music.pickle") -> None:
    with open(filename, "wb") as file:
        pickle.dump(data, file)
        print(f"{filename} saved.")


def load_data_pickle(filename: str = "music.pickle") -> dict[str, list[str]]:
    with open(filename, "rb") as file:
        data = pickle.load(file)
    return data

def add_band(data: dict[str, list[str]]) -> None:
    band = input("Please new band: ")

    if band in data:
        print("Such band exists")
        return

    data[band] = []
    print("New band added to the list")


def add_album(data: dict[str, list[str]]) -> None:
    band = input("Please input band name: ")

    if band not in data:
        print("Such band does not exist")
        return

    album = input("Please input album name: ")

    if album in data[band]:
        print("Album already exists")
        return

    data[band].append(album)
    print("New album added to the list")


data: dict[str, list[str]] = {}
add_band(data)
add_album(data)

save_data_json(data)
save_data_pickle(data)

data_pkl = load_data_pickle(filename="music.pickle")
data_json = load_data_json(filename="music.json")

