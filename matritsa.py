A = []

for i in range(9):
    qator = []
    for j in range(9):
        qator.append(i + j)   # misol uchun sonlar
    A.append(qator)

sumA = 0

for i in range(9):
    for j in range(9):
        if i == 0 or i == 8 or j == 0 or j == 8:
            sumA += A[i][j]

print("A bo‘limidagi bo‘yalgan elementlar yig‘indisi:", sumA)



# 9x9 matritsa yasash (oddiy sikllar bilan)
A = []

for i in range(9):
    qator = []
    for j in range(9):
        qator.append(i + j)
    A.append(qator)

# B bo‘limi yig‘indisi (diagonallar)
sumB = 0

for i in range(9):
    for j in range(9):
        if i == j or i + j == 8:   # 2 ta diagonal
            sumB += A[i][j]

print("B bo‘limi (diagonallar) yig‘indisi:", sumB)

# D bo‘limi yig‘indisi (yuqori va pastki uchburchaklar)
sumD = 0
for i in range(9):
    for j in range(9):
        if i + j <= 8 or j >= i:  # rasmga qarab yuqori va pastki uchburchaklarni qamrab olamiz
            sumD += A[i][j]

print("D bo‘limi yig‘indisi:", sumD)

# E bo‘limi yig‘indisi (markaziy romb)
sumE = 0
for i in range(9):
    for j in range(9):
        if abs(i - 4) + abs(j - 4) <= 4:  # markaziy romb uchun shart
            sumE += A[i][j]

print("E bo‘limi yig‘indisi:", sumE)

