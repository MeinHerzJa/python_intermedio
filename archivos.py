import numbers


def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    name = ["Livana", "Adriana", "Lorena"]
    with open("./archivos/numbers.txt", "a", encoding= "utf-8") as f:
        for names in name:
            f.write(names)
            f.write("\n")


def run():
    write()


if __name__ == "__main__":
    run()