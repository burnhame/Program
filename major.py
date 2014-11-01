Program
=======
name = raw_input("What is your name?")
print "hello", name

questionOne = raw_input ("Do you like science? y/n")

if questionOne == "y":
    print "you should major in science!"
elif questionOne == "n":
    questionTwo = raw_input ("Do you like math? y/n")
    if questionTwo == "y":
        print "You should major in math!"
    elif questionTwo == "n":
        questionThree = raw_input("Do you like movies? y/n")
        if questionThree == "y":
            print "you should major in CAMS!"
        elif questionThree == "n":
            while questionThree != "y":
                print "please answer honestly"
                questionThree = raw_input("Do you like movies? y/n")
                if questionThree == "y":
                    print "You should major in film!"
print "congrats!"
