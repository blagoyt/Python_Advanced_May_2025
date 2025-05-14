from collections import deque


petrol_pumps_num = int(input())
petrol_pumps = deque()

for _ in range(petrol_pumps_num):
    current_fuel, current_distance =  input().split()
    petrol_pumps.append({"fuel": int(current_fuel), "distance": int(current_distance)}) # ({"fuel": 5, "distance": 3})

start_position = 0
stops = 0

while stops < petrol_pumps_num:
    fuel = 0
    for i in range(petrol_pumps_num):
        fuel += petrol_pumps[i]["fuel"]
        distance = petrol_pumps[i]["distance"]
        if fuel < distance:
            petrol_pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(start_position)
