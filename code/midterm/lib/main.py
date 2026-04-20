# main.py

from device import Roomsensor

Kitchen = Roomsensor("Kitchen",35,80,600)
Bedroom = Roomsensor("Bedroom",20,30,30)
Balcony = Roomsensor("Balcony",10,70,100)

sensors = [Kitchen,Bedroom,Balcony]

for s in sensors:
    s.show_info()
    print(f"Comfort: {s.comfort_level()} | Light: {s.light_status()}")
    print("-"*20)

counts = {
    "Comfortable": 0,
    "Normal": 0,
    "Warning": 0
}
for s in sensors:
    status = s.comfort_level()
    if status in counts:
        counts[status]+= 1
print(f"Comfortabale: {counts['Comfortable']}")
print(f"normal: {counts['Normal']}")
print(f"Warning: {counts['Warning']}")