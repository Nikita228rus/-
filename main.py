from algoritms import *


def menu():
    print("1- расширенный алгортим Евклида\n"
          "2- алгоритм быстрого воздедения в степень\n"
          "3- алгоритм быстрого возведения в степень по модулю\n"
          "4- вычисление символа Якоби\n"
          "5- алгоритмы проверки на простату\n"
          "6- генерация простого числа заданной размерности\n"
          "7- решение сравнения первой степени\n"
          "8- решение сравнения второй степени\n"
          "9- решение системы сравнений\n"
          "10- построение конечного поля и реализация операций над данным полем\n"
          "11- каноническое представление числа\n"
          "12- символ Лежандра\n"
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
    elif choose == "6":
        k = int(input("Задайте размерность:\t"))
        generation_simple(k)
    elif choose == "7":
        print(first_degree())
    elif choose == "9":
        print(system_first_degree())
    elif choose == "11":
        n = int(input("Задайте число:\t"))
        print(factorization(n))
    elif choose == "12":
        a, n = map(int, input("Задайте числа:\t").split())
        print(symbol_legendre(a, n))


def second_degree():
    """x^2 = a (mod p); (a, p) = 1"""
    a, p = map(int, input().split())
    m = test_miller(p)
    d = euclid_algorithm2(a, p)
    if m is False or d[0] != 1:
        return f"Уравнение не имеет решений"
    elif m is True and d[0] == 1:
        pass


menu()









