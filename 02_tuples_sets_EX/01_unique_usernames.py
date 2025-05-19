# n = int(input())

unames = set()

for _ in range(int(input())):
    # names = input()
    unames.add(input())

# for name in unames:
#     print(name)
# print("\n".join(unames))
print(*unames, sep="\n")