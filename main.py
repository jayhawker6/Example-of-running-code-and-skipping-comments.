#
#š Hi, Iām @jayhawker6
#š Iām interested in Python, Dart, Java, And Kotlin.
#š± Iām currently learning Kotlin.
#šļø Iām looking to collaborate on My small game i've been working on, ByteBase.
#š« You can reach me by messaging or creating bug/issue reports or pull requests.
#-And remember kids:
#
#"People who care about code effeciency are weebs.
#My code is ugly and yours can be too!"
#
#      -Ghandi
#

print('hello world')


def commenttest():
    #This is my prefab from VS 2019, used in a game I am working on called bytebase.
    while True:
        try:
            response = int(
                input("""
        Would you like to see what happens when you try to print a comment? If so, then please press 1. If you would like to run without the comment, please press 2. If you would like to end this call, press 0. Thank you!
        
"""))
        except ValueError:
            print("Please answer with one of the stated integers. Thank you!")
            continue
        if response == 1:
            #print('Testing, Testing, Testing')
            break
        elif response == 2:
            print('Testing, Testing, Testing')
            break
        elif response == 0:
            quit('The call was ended')
        else:
            print("This is not an option!")
            continue


commenttest()
while True:
    try:
        wishfor = int(
            input("""Press 1 to end the call. Press 2 to retry
				"""))
    except ValueError:
        print('Please use one of the stated integers.')
        continue
    if wishfor == 1:
        quit('The call was ended')
    elif wishfor == 2:
        commenttest()
        continue
    else:
        print('not an option!')
        continue
quit('The call was ended')