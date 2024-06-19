def get_starting_number():
    while True:
        try:
            num = int(input("How many bottles of beer on the wall? "))
            if num >= 1:
                return num
        except ValueError:
            pass

def sing(start):
    for i in range(start, 0, -1):
        plural = "" if i == 1 else "s"
        print(f"{i} bottle{plural} of beer on the wall, {i} bottle{plural} of beer.")
        print("Take one down, pass it around,", end=" ")
        if i - 1 == 0:
            print("no more bottles of beer on the wall!")
        else:
            print(f"{i-1} bottle{'' if i-1 == 1 else 's'} of beer on the wall.")
