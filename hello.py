"""Kodune töö nr 1."""

def main():
    """1.Programm küsib sisendit: (input)."""
    name = input("What's your name? ")
    if name == "":
        print("Name was not inserted!")
    school = input("Where do you study? ")
    if school == "":
        print("School was not inserted!")
    print(name + ", welcome to " + school)


def ex01():
    """2.Arvuta kehamassi indeks kasutades sisendit (input)."""
    mass = float(input("Palun sisestage oma mass (kg): "))
    height = float(input("Palun sisestage oma pikkus (m): "))

    kehamassiindeks = mass / height ** 2

    if kehamassiindeks > 25.0:
        keha = "ülekaaluline"
    elif kehamassiindeks < 18.5:
        keha = "alakaaluline"
    elif kehamassiindeks >= 18.5 and kehamassiindeks <= 24.9:
        keha = "normaalkaal"
    print(str(kehamassiindeks) + ", " + str(keha))


if __name__ == '__main__':
    main()
    ex01()