import re

text = """А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666"""

private_car_pattern = r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b'
private_cars = re.findall(private_car_pattern, text)
print('Список номеров частных автомобилей:', private_cars)

taxi_pattern = r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}\b'
taxis = re.findall(taxi_pattern, text)
print('Список номеров такси:', taxis)
