inputHour = input("몇 시입니까?")
inputMin = input("몇 분 입니까?")
inputTime = input("요리하는데 몇 분이 걸립니까?")

hours = int(inputHour)
minuit = int(inputMin)
time = int(inputTime)

print(hours, minuit)
print(time)

if time+minuit >= 60 and hours < 23 :
    print (hours + 1 , time+minuit-60)

elif time+minuit >= 60 and hours >= 23 :
    print (0 , time+minuit-60)
    

elif time+minuit < 60 :
    print (hours, time+minuit)
    
