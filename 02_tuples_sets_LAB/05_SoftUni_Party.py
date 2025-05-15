n = int(input())

reservations = set()

for _ in range(n):
    res_num = input()
    reservations.add(res_num)


reservation = input()

while reservation != "END":
    reservations.remove(reservation)
    reservation = input()

print(len(reservations))

sorted_reservation = sorted(reservations)
print(*sorted_reservation, sep="\n")