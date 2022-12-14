def divisors(num):
    try:
        if num < 0:
            raise ValueError("Debes ingresar un número positivo (Mayor que cero)")
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        num = int(input('Ingrese un número: '))
        print(divisors(num))
        print("Termino mi programa.")
    except ValueError:
        print("Debes ingresar un número!")


if __name__ == "__main__":
    run()