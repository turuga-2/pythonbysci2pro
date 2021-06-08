import sys


def main():
    # creating lists
    l = list()
    print(l, type(l))
    print(f"The length of the list is {len(l)}")

    field = [2, 4, 6, 8, 10]
    print(f"the field is {field} and it's length is {len(field)}")
    print(dir(field))
    # checking if an object is a member of the list
    print(2 in field)
    print(13 not in field)
    # adding items to a list
    field1 = field + [1, 3, 5, 7, 9]
    print(f"field1 = {field1}")
    print(id(field))
    print(id(field1))
    # when you want to copy the objects of a list to another list use the copy() function
    field2 = field1.copy()
    print(f"field2 ={field2}")
    field2 += [11, 13, 15]
    print(f"field2 ={field2}")
    # lengths, min and max values
    print(f"The maximum value is {max(field2)}")
    print(f"The minimum value is {min(field2)}")

    # indexing  remember counting starts at 0
    print(f"the first item is {field2[0]}")
    print(f"8 is at {field2.index(8)}")

    # when an asterisc is used on lists it produces the same number x times
    # cannot multiply a list by another list

    trial = [2] * 10
    # here the order doesn't matter.
    print(f"trial = {trial}")
    print(f"trial has a length of {len(trial)}")

    # counting the instances of an object in a list or the items in a list
    field += [8] * 5
    print(field)
    print(f" There are {field.count(8)} instances of 8 in field")

    # also applies to strings
    print(f"sarah" * 4)

    # slices
    print(field[0:4])
    print(field[0:9:3])
    # range function used to create a generator
    field3 = list(range(10))
    print(field3)
    print(field3[1:6])
    print(field3[0:10:2])
    # replacing using index
    field3[4] = 24
    print(f"The new field3 is {field3}")

    # deleting an object from the list
    print(len(field3))
    del field3[4]
    print(len(field3))

    # appending items to a list
    # we use the append() method
    field4 = list()
    field4.append(20)
    print(field4)




    return 0


if __name__ == "__main__":
    sys.exit(main())
