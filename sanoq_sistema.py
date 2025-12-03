# 2

n = int(input("Son kiriting: "))

natija = ""

temp = n
while temp > 0:
    qoldiq = temp % 2
    natija = str(qoldiq) + natija
    temp //= 2

print("2-lik:", natija)


# 8

natija8 = ""
temp = n
while temp > 0:
    qoldiq = temp % 8
    natija8 = str(qoldiq) + natija8
    temp //= 8

print("8-lik:", natija8)


# 16

digits = "0123456789ABCDEF"
natija16 = ""
temp = n
while temp > 0:
    qoldiq = temp % 16
    natija16 = digits[qoldiq] + natija16
    temp //= 16

print("16-lik:", natija16)

