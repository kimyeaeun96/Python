user_input = input("몇번째 줄까지 입력할까요?")
line = int(user_input)

for i in range (0, line) :
    for j in range (line-i) :
        print("*", end="")
    print()
