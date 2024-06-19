def get_starting_number():
    while True:
        try:
            num = int(input("How many bottles of beer on the wall? "))
            if num >= 1:
                return num
        except ValueError:
            pass
def sing(start):
    flag = True
    while flag:
        plural = "" if start == 1 else "s"
        print(f"{start} bottle{plural} of beer on the wall, {start} bottle{plural} of beer.")
        start -= 1
        plural = "" if start == 1 else "s"
        print("Take one down, pass it around,", end=" ")
        if start == 0:
            print("no more bottles of beer on the wall!")
            flag = False
        else:
            print(f"{start} bottle{plural} of beer on the wall.")

