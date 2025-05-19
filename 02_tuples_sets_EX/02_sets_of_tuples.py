n, m = map(int, input().split()) #казваме към какво да мапнем в случая int и какво да мапнем значи input().split()

n_set = set() #n_set = {input() for _ in range(n)}
m_set = set() #m_set = {input() for _ in range(m)}

for _ in range(n):
    n_set.add(input())  #Може и към инт да ги сложим add(int(input()))

for _ in range(m):
    m_set.add(input())  #Отново можем

result = n_set.intersection(m_set)  #n_set & m_set

print(*result, sep="\n")