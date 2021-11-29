import random


def test_miller(n):
    exp = n - 1
    a = random.randint(2, n - 2)
    while not exp & 1:
        exp >>= 1

    if pow(a, exp, n) == 1:
        return True

    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True
        exp <<= 1
    return False


def generation_simple():
    k = random.randint(5, 10)

    dvoi4noe_4islo = []
    while k != 0:
        bit = random.randint(0, 1)
        dvoi4noe_4islo.append(bit)
        k = k - 1

    del dvoi4noe_4islo[-1]
    dvoi4noe_4islo.append(1)
    del dvoi4noe_4islo[0]
    dvoi4noe_4islo.insert(0, 1)

    p = 0
    for j in range(len(dvoi4noe_4islo)):
        if dvoi4noe_4islo[j] == 1:
            p = p + 2 ** j
        else:
            continue

    spisok = []
    for z in range(100):


        spisok.append(test_miller(p))

    if spisok[z]==True:


            return print("Число простое", p, "Число повторений", len(spisok))

    else:
            generation_simple()

generation_simple()