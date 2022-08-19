# True = male and False = Female

def what_is_your_gender(gender,sex):
    if gender == True and sex == True:
        return print("Your male")
    elif gender == True and sex == False:
        return print("Your a transgender man")
    elif gender == False and sex == True:
        return print("Your a transgender woman")
    elif gender == False and sex == False:
        return print("Your female")
    else:
        return print("Error")

what_is_your_gender(True,True)
