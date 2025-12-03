# 10-likdan 2-likka o'tkazish (tayyor funksiyasiz)

n = int(input("Son kiriting: "))

natija = ""

temp = n
while temp > 0:
    qoldiq = temp % 2
    natija = str(qoldiq) + natija
    temp //= 2

print("2-lik:", natija)
