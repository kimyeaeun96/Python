user_input = input("몇 줄을 입력할까요?")
line = int(user_input)

for i in range (0, line):
    print(" "*i + "*"*(line-i))
