def gretting(x):
    print("Hello")

    if x < 12:
        print("Good Morning")
    else:
        print("Good Afternoon")    

time = int(input("What time is it? "))

gretting(time)