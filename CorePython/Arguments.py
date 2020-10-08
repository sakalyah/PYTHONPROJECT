# POsitional Arguments
def person(name, age, mob=9848249243):  # mob is Default Argument
    print(name, age, mob)
    print(name, age - 10, mob)


person("Harish", 26, 8124757026)
# person(28,"Soundarya")
person(name="Soundarya", age=25)  # Keyword Arguments


# Variable Length Arguments, Tuple Data.
def sum(a, *b):
    c = a
    for i in b:
        c = c + i
    return c


b = sum(1, 2, 3, 4, 5)
print(b)


# Keyworded Variable Length Arguments.Dictionary pairs
def man(name, **details):
    print(name)
    print(details)
    print(details.items())


man("Harish", age=26, city="Chennai", Mob=8124757026)
