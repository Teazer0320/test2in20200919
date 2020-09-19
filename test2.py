num = int(input("請輸入一個數字: "))
for x in range(num):
    tmp = num
    for y in range(tmp):
        print("* ")
        tmp-=1
    print("\n")

