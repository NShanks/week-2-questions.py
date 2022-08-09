age = input("What is your age?")

if int(age) < 18:
    print(age,"? Where are your parents? Go home and study or something.")
elif 18 <= int(age) <= 65:
    print("You're", int(age),"you should be getting ready for retirement. It's how many years away?", 65-int(age), "? Good. Plenty of time to start.")
else:
    print("You're", int(age), "years young. Congrats!")