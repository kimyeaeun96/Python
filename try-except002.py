try:
    f = open("nofile.txt", "r")
    print(f)
except FileNotFoundError:
    print("파일이 없습니다.")
