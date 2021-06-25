import sys
import random
import string


def main():
    # 1. Creating dictionaries
    exe0 = dict()
    print(exe0, type(exe0))

    # literal way ya kuform dictionary
    exe1 = {"triangle": 'a', "circle": 'b'}
    print(exe1, type(exe1))

    # using key word arguments
    exe2 = dict(triangle='a', circle='b')
    print(exe2, type(exe2))
    # one can mix and match the various ways of creating dictionaries to create one
    list1 = random.choices(range(15), k=15)
    print(f"list1 = {list1}")
    list2 = random.choices(range(15), k=15)
    print(f"list2 = {list2}")
    print(list(zip(list1, list2)))
    exe3 = dict(zip(list1, list2))
    print(exe3)
    # getting items from dictionaries
    # you'll use the keyword
    exe4 = dict(zip(string.ascii_lowercase, list1))
    print(exe4)
    print(exe4['b'])
    # get function
    print(f"default value is {exe3.get(3, 456)}")

    # modifying the content of the dictionary
    counties = {
        'nairobi': 47,
        'Mombasa': 10,
        'Kisumu': 23,
        'Nakuru': 34,
        'Kwale ': 25,
        'Nyali': 39,
    }
    print(counties)
    # changing the values
    counties['Mombasa'] = 144
    print(counties)
    # adding values
    # 1
    counties['Kiambu'] = 40
    print(f"after addition = {counties}")
    print(f"Kisii", counties.setdefault('Kisii', 32))
    print(counties)
    del counties['Kisumu']
    print(counties)
    # check for membership
    print("Is Kisumu in counties? ", 'Kisumu'in counties)
    # checking the length
    print((len(counties)))

    # casting the dictionary to a list
    # here only the keys are displayed
    print(list(counties))

    # methods in dict
    # dict.items
    print(counties.items())
    for key, value in counties.items():
        print(f"The county {key} is number {value}")


    return 0


if __name__ == "__main__":
    sys.exit(main())
