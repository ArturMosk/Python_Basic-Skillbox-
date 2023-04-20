import requests
import json
from typing import List


def get_and_output_data_about_pilot_homeworld(planet_link: str) -> str:
    """
    Функция, реализующая получение информации о родной планете пилота.

    :param planet_link [str]: адрес веб-страницы родной планеты пилота
    :return: название родной планеты пилота
    """
    planet_request = requests.get(planet_link)
    planet_full_data = json.loads(planet_request.text)
    planet_name = planet_full_data['name']

    return planet_name


def get_and_output_data_about_pilots(pilots: List[str]) -> List[dict]:
    """
    Функция, реализующая получение информации о пилотах корабля.

    :param pilots List[str]: список пилотов корабля
    :return List[dict]: список с информацией о каждом пилоте корабля
    """
    pilots_data = []
    for pilot in pilots:
        pilot_request = requests.get(pilot)
        pilot_full_data = json.loads(pilot_request.text)
        pilot_data = {'name': pilot_full_data['name'],
                      'height': pilot_full_data['height'],
                      'mass': pilot_full_data['mass'],
                      'homeworld': get_and_output_data_about_pilot_homeworld(pilot_full_data['homeworld']),
                      'homeworld_link': pilot_full_data['homeworld']
                      }
        pilots_data.append(pilot_data)

    return pilots_data


falcon_request = requests.get('https://swapi.dev/api/starships/10/')
falcon_full_data = json.loads(falcon_request.text)
falcon_data = {'name': falcon_full_data['name'],
               'max_atmosphering_speed': falcon_full_data['max_atmosphering_speed'],
               'starship_class': falcon_full_data['starship_class'],
               'pilots': get_and_output_data_about_pilots(falcon_full_data['pilots'])
               }

print(json.dumps(falcon_data, indent=4))
with open('Millennium_Falcon.json', 'w') as file:
    json.dump(falcon_data, file, indent=4)
