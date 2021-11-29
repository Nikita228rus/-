from algoritms import *


def menu():
    print("1- расширенный алгортим Евклида+\n"
          "2- алгоритм быстрого воздедения в степень+\n"
          "3- алгоритм быстрого возведения в степень по модулю+\n"
          "4- вычисление символа Якоби+\n"
          "5- алгоритмы проверки на простату+\n"
          "6- генерация простого числа заданной размерности\n"
          "7- решение сравнения первой степени+\n"
          "8- решение сравнения второй степени\n"
          "9- решение системы сравнений+\n"
          "10- построение конечного поля и реализация операций над данным полем\n"
          )
    choose = input(">>>\t")
    if choose == "1":
        print(euclid_algorithm())
    elif choose == "2":
        print(fast_pow())
    elif choose == "3":
        print(fast_pow_mod())
    elif choose == "4":
        print(symbol_legendre())
    elif choose == "5":
        check_func(1000)
    elif choose == "7":
        print(first_degree())
    elif choose == "9":
        print(system_first_degree())


def second_degree():
    """x^2 = a (mod p); (a, p) = 1"""
    a, p = map(int, input().split())
    m = test_miller(p)
    d = euclid_algorithm2(a, p)
    if m is False or d[0] != 1:
        return f"Уравнение не имеет решений"
    elif m is True and d[0] == 1:
        pass


def symbol_legendre():
    a, n = map(int, input().split())

    b = pow(a, int((n-1)/2), n)

    if b != 1:
        b = b - n

    return b


def symbol_jacobi():
    a, n = map(int, input().split())
    check = test_miller3(n)

    if check is False:
        canon = []
        while test_miller3(n) is False:
            i = 2
            if test_miller3(i) is True:
                if n % i == 0:
                    n = n / i
                    canon.append(n)
                    i += 1
                else:
                    i += 1
            else:
                i += 1
        print(canon)


def symbol_jacobi2():
    a, n = map(int, input().split())
    a1 = a
    k = 0
    g = 1
    while a1 % 2 == 0:
        a1 = int(a1 / 2)
        k += 1

    print(f'{a} = 2^{k} * {a1}')
    print(k)

    if k % 2 == 0:
        s = 1

    def s_c(k):
        if k % 2 == 0:
            s = 1
            return s
        elif k % 2 != 0:
            if (n - 1) % 8 == 0 or (n + 1) % 8 == 0:
                s = 1
                return s
            elif ((n - 3) % 8 == 0) or ((n + 3) % 8 == 0):
                s = -1
                return s

    print(s_c(k))


def factorization():
    n = int(input())
    l = []

    if n < 5:
        if n == 2:
            l = [2]
        elif n == 3:
            l = [3]
        elif n == 4:
            l = [2, 2]
        return l
    else:
        check = test_miller4(n)
        if check is True:
            l.append(n)
            return l

        else:
            i = 7
            l_i = [2, 3, 5]

            for i in l_i:
                while n % i == 0:
                    n = int(n / i)
                    l.append(i)
            if n > 5:
                check = test_miller4(n)
                if check is True:
                    l.append(n)
                else:
                    for i in range(7, n, 2):
                        check_i = test_miller4(i)
                        if check_i is True:
                            while n % i == 0:
                                n = int(n / i)
                                l.append(i)
                        else:
                            pass
                return l
            else:
                return l


print(factorization())
