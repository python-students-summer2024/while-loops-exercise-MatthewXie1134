def get_starting_number():
    while True:
        try:
            num = int(input("How many bottles of beer on the wall? "))
            if num >= 1:
                return num
        except ValueError:
            pass
def sing(start):
    num = start
    while num > 0:
        plural = "" if num == 1 else "s"
        print(f"{num} bottle{plural} of beer on the wall, {num} bottle{plural} of beer.")
        num -= 1
        plural = "" if num == 1 else "s"
        print("Take one down, pass it around,", end=" ")
        if num == 0:
            print("no more bottles of beer on the wall!")
        else:
            print(f"{num} bottle{plural} of beer on the wall.")
