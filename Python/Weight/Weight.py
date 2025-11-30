unit = input("(K)g or (L)bs: ")
weight = int(input("Weight: "))


if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0,45
    print("Weight in Kgs: " + str(converted))

