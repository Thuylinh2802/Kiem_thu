def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def test():
    money = input()
    if is_number(money) == False:
        print("Input is invalid")
    elif is_number(money) == True:
        money = float(money)
        if(money < 0.01):
            print("Input is invalid")
        elif(0.01 <= money and money <= 100):
            print("4%")
        elif(100.01 <= money and money <= 999.99):
            print("6%")
        elif(money >= 1000):
            print("9%")

test()