user_age = input("나이를 입력하세요.")
intAge = int(user_age)

if intAge >= 20 :
    print("성인")
    if intAge % 2 == 0 :
        print("나이가 짝수인 성인")
elif intAge < 20 :
    print("미성년자")
    if intAge % 2 != 0 :
        print("나이가 홀수인 미성년자")
        
