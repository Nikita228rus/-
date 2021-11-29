import random
import sympy


def euclid_algorithm():
    a, b = map(int, input("Введите два числа: ").split())
    r = [a, b]
    x = [1, 0]
    y = [0, 1]

    i = 0
    while r[i] != 0:
        if r[i + 1] != 0:

            q = (r[i] // r[i+1])
            c = r[i] - q * r[i+1]
            a = x[i] - q * x[i+1]
            b = y[i] - q * y[i+1]

            x.append(a)
            y.append(b)
            r.append(c)
            i += 1

        elif r[i + 1] == 0:
            break

    d = r[i]
    u = x[i]
    v = y[i]

    choose = input("1 - линейное представление НОД.\n2 - выход.\n")
    if choose == "1":
        return f"{d} = {r[0]} * {u} + {r[1]} * {v}"
    else:
        return d


def euclid_algorithm2(a, b):

    r = [a, b]
    x = [1, 0]
    y = [0, 1]

    i = 0
    while r[i] != 0:
        if r[i + 1] != 0:

            q = (r[i] // r[i + 1])
            c = r[i] - q * r[i + 1]
            a = x[i] - q * x[i + 1]
            b = y[i] - q * y[i + 1]

            x.append(a)
            y.append(b)
            r.append(c)
            i += 1

        elif r[i + 1] == 0:
            break

    d = r[i]
    u = x[i]
    v = y[i]

    return [d, u, v]


def first_degree(a, b, m):
    d = euclid_algorithm2(a, m)
    x = []

    if b % d[0] != 0:
        return f"Сравнение {a}x = {b} (mod {m}) не имеет решений."

    elif d[0] != 1:
        a1 = int(a/d[0])
        b1 = int(b/d[0])
        m1 = int(m/d[0])
        d1 = euclid_algorithm2(a1, m1)
        if d1[0] == a1 * d1[1] + m1 * d[2]:
            x1 = b1 * d1[1]
            while x1 < 0:
                x1 += m1
            for i in range(0, d[0]):
                c = x1 + m1 * i
                x.append(c)

    elif d[0] == 1:
        if d[0] == a * d[1] + m * d[2]:
            x1 = b * d[1]
            while x1 < 0:
                x1 += m
            while x1 > m:
                x1 -= m
            x.append(x1)

    return f"x = {x} (mod {m})"


def system_first_degree():
    n = int(input("Размерность системы:\t"))
    massive = []

    for i in range(n):
        massive.append([])
    print("x = a (mod m)")
    for j in range(len(massive)):
        a, m = map(int, input(f"{j+1}) a, m:\t").split())
        massive[j].append(a)
        massive[j].append(m)

    i = 0
    j = i + 1
    d_list = []
    while i != len(massive) - 1:
        while j != len(massive):
            d = euclid_algorithm2(massive[i][1], massive[j][1])
            d_list.append(d[0])
            j += 1
        i += 1
        j = i + 1

    if d_list.count(1) != len(d_list):
        return f'Модули попарно невзаимно просты :('

    elif d_list.count(1) == len(d_list):
        m = 1
        for i in massive:
            m *= i[1]

        m_list = []
        for i in massive:
            mj = m/i[1]
            m_list.append(int(mj))

        n_list = []
        for i in range(len(massive)):
            nj = euclid_algorithm2(massive[i][1], m_list[i])
            if nj[2] < 0:
                nj[2] += massive[i][1]
            n_list.append(nj[2])

    x = 0
    for i in range(n):
        x += massive[i][0]*n_list[i] * m_list[i]
    while x > m:
        x -= m

    return f"x = {x} (mod {m})"


def test_miller3(n):
    a = random.randint(1, n-2)
    exp = n - 1
    while not exp & 1:
        exp >>= 1

    if pow(a, exp, n) == 1:
        return True

    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True
        exp <<= 1

    return False


def symbol_legendre():
    a, n = map(int, input().split())

    b = pow(a, int((n-1)/2), n)

    if b != 1:
        b = b - n

    return b


def test_fer(n, a):
    c = pow(a, n-1, n)
    if c == 1:
        return True
    else:
        return False


"""!!!"""


def test_miller(n, a):
    exp = n - 1
    while not exp & 1:
        exp >>= 1

    if pow(a, exp, n) == 1:
        return True

    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True
        exp <<= 1
    return False


"""!!!"""


def test_sol(n, a):

    while True:
        if n % 2 != 0:
            break

    "a = random.randint(2, n - 2)"
    r = pow(a, (n-1) // 2, n)
    if r != 1 and r != n-1:
        return False

    elif r == pow(sympy.jacobi_symbol(a, n), 1, n):
        return True
    else:
        return False


def test_miller2(n, a):
    s = 0
    m = n - 1

    while m % 2 == 0:
        m = m / 2
        s += 1
    r = int((n-1) / pow(2, s))
    '''n-1 = 2**s r'''
    y = pow(a, r, n)
    if y != 1 and y != n-1:
        j = 1
        while j <= s - 1 and y != n - 1:
            y = pow(y, 2, n)
            if y == 1:
                return False
            j += 1

        if y != n - 1:
            return False

    return True


def check_func(k=1000):
    result_list = []
    n = int(input("Подозреваемое число: "))
    print("1 - Тест Ферма\n2 - Тест Соловея-Штрассена\n3 - Тест Миллера-Рабина")
    choose_test = input("Выберите тест: ")
    if choose_test == "1":
        for i in range(k):
            a = random.randint(2, n-2)
            c = test_fer(n, a)

            if c is True:
                result_list.append(1)
            elif c is False:
                result_list.append(0)
        if result_list.count(1) == len(result_list):

            return print(f"{n} - простое число.")
        else:
            ver = int((result_list.count(1) / len(result_list)) * 100)
            return print(f"{n} - составное число.\nВероятность ошибки теста {ver}%")

    if choose_test == "2":
        for i in range(k):
            a = random.randint(2, n-2)
            c = test_sol(n, a)

            if c is True:
                result_list.append(1)
            elif c is False:
                result_list.append(0)
        if result_list.count(1) == len(result_list):
            return print(f"{n} - простое число")
        else:
            ver = int((result_list.count(1) / len(result_list)) * 100)
            return print(f"{n} - составное число.\nВероятность ошибки теста {ver}%")

    if choose_test == "3":
        for i in range(k):
            a = random.randint(2, n - 2)
            c = test_miller2(n, a)

            if c is True:
                result_list.append(1)
            elif c is False:
                result_list.append(0)
        if result_list.count(1) == len(result_list):
            return print(f"{n} - простое число")
        else:
            ver = int((result_list.count(1) / len(result_list)) * 100)
            return print(
                f"{n} - составное число.\nВероятность ошибки теста {ver}%")

    if choose_test != "1" or choose_test == "2" or choose_test != "3":
        print("Неверный выбор. Попробуйте снова...\n")

        check_func()


def fast_pow():
    print("а - основание степени\nn - показатель степени")
    a, n = map(int, input("Ввод a, n:\t").split())
    n1 = n
    n2 = []
    x = 1

    while n != 0:
        h = n % 2
        n2.append(h)
        n = n // 2
    n2.reverse()

    for i in range(len(n2)):
        x = x * pow(a, int(n2[i]) * pow(2, i))

    return f"{a} в степени {n1} = {x}"


def fast_pow_mod():
    print("а - основание степени\nn - показатель степени\nm - модуль")
    a, n, m = map(int, input("Ввод a, n, m:\t").split())
    n1 = n

    n = format(n, "b")

    for i in range(len(n)):
        if i == 0:
            c = pow(a, int(n[0]))
        else:
            c = pow(c, 2, m)
            if int(n[i]) == 1:
                c = pow(c * a, 1, m)

    return f'{a} в степени {n1} сравнимо с {c} по модулю {m}'


def test_miller4(n):
    s = 0
    m = n - 1
    a = random.randint(2, n-2)

    while m % 2 == 0:
        m = m / 2
        s += 1
    r = int((n-1) / pow(2, s))
    '''n-1 = 2**s r'''
    y = pow(a, r, n)
    if y != 1 and y != n-1:
        j = 1
        while j <= s - 1 and y != n - 1:
            y = pow(y, 2, n)
            if y == 1:
                return False
            j += 1

        if y != n - 1:
            return False

    return True
