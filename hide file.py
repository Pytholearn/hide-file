import os 

print("\n")

hide_option = input("you want to hide folders and file (y/n) ? or hit enter to show option : ")

if(hide_option == ""):
    show_option = input("you want folders and file (y/n) ? : ")

    if (show_option == "y"):
        os.system("attrib -h /s /d")
        print("your folders and file are visible!")
    elif(show_option == "n"):
        print("ok good by bro")

if (hide_option == "y"):
    os.system("attrib +h /s /d")
    print("your folders and file are hidden !!")
elif(hide_option == "n"):
    print("ok goof by bri")