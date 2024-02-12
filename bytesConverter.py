main = input("Enter what you have to convert and in what\n For example mb to gb, gb to mb, gb to tb, tb to gb only into this format")


if main == "mb to gb":
    mb = float(input("Enter the data in mb\n"))
    gb = mb / 1024
    print(mb, " is equal to ", gb, " gb")
elif main == "gb to mb":
    gb = float(input("Enter the data in gb\n"))
    mb = gb * 1024
    print(gb, " is equal to ", mb, " mb")
elif main == "gb to tb":
    gb = float(input("Enter the data in gb\n"))
    tb = gb/1024
    print(gb, " is equal to ", tb, " tb")
elif main == "tb to gb":
    tb = float(input("Enter the data in tb\n"))
    gb = tb * 1024
    print(tb, "gb is equal to ", gb, "gb")
else:
    print("Please enter as per given the starting instruction");
