item1_price = 0
item2_price = 1.5
item3_price = -100.4
item4_price = 9.4


def findleast(*args):
    print("Find the least number for argument(s): " + str(args))

    leastvalue = 0
    temp = args[0]

    for x in args:
        if x < temp:
            temp = x
        leastvalue = temp

    return leastvalue


print("Least number: " + str(findleast(item1_price, item2_price, item3_price, item4_price)))
