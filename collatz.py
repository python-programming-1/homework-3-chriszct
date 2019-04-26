def collatz(num) :
    while num != 1 :
        if num % 2 == 0 :
            num = num / 2
        else :
            num = num * 3 + 1
        print(int(num))


while True:
    print("Please enter an integer: ")
    num = input()
    
    try:
        num = int(num)
        collatz(num)
    except:
        print("you didnt enter an integer, please try again.")

