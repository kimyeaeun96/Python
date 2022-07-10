list = [0, 1, 2, 3]

for i in range(6):
    try:
        print(list[i])
    except IndexError:
        print("해당하는 인덱스가 없습니다.")

