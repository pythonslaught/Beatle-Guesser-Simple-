possibilities = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"]

answer = input("Does that Beatle play the Guitar? (yes/no) ")

if answer == "yes":
    exclusions = ["Paul McCartney", "Ringo Starr"]
    possibilities = list(set(possibilities) - set(exclusions))
    answer = input("Does that Beatle wear glasses? (yes/no) ")
    if answer == "yes":
        print("The Beatle is John Lennon!")
    elif answer == "no":
        print("The Beatle is George Harrison!")

elif answer == "no":
    exclusions = ["John Lennon", "George Harrison"]
    possibilities = list(set(possibilities) - set(exclusions))
    answer = input("Does your Beatle play the drums? (yes/no) ")
    if answer == "yes":
        print("The Beatle is Ringo Starr!")
    elif answer == "no":
        print("The Beatle is Paul McCartney!")

else:
    print("Invalid answer.")
    #answer = input("Does that Beatle play the Guitar? (yes/no) ")




