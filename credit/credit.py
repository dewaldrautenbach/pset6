from sys import argv
#from cs50 import get_string

def isLowerChar(input):
    if str.islower(input):
        return True
    else:
        return False

def isUpperChar(input):
    if str.isupper(input):
        return True
    else:
        return False;


def  convertCase(toConvert):
    if str.isupper(toConvert):
        output = ord(toConvert) - 65
        print(f"{output}")
    else:
        output = ord(toConvert) - 97
        return chr(output)


def GetCypherCharLower(c, key):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        end = 122
    if isLowerChar(c) == True:
        newCharLower = str(ord(c) + ord(convertCase(key)))
    else:
        newCharLower = 0
    while int(newCharLower) > end:
        newCharLower -= 26
        if newCharLower < end:
            break
    return (newCharLower)


def  GetCypherCharUpper(d, key):
        end = 0
        if ord(d) >= ord("A") and ord(d) <= ord("Z"):
            end = 90
            if isUpperChar(d) == True:
                newCharUpper = str(ord(d) + ord(convertCase(key)))
            else:
                newCharUpper = 0
            while int(newCharUpper) > end:
                newCharUpper -= 26
                if newCharUpper < end:
                    break
            return (newCharUpper)
    





k = argv[1] = "dewald"
i = "Zander" #get_string("Plaintext: ")
length = len(i) #plaintext
modLength = len(k) #key


if len(argv) == 0:
    print("No argument passed")
    exit
elif str.isalpha(argv[1] == 0):
    print("Invalid text entered!")
    exit
elif argc > 2:
    print("Too many arguments")

counter = -1

print("ciphertext: ", end="")

for n in range(length):
    a = i[n]

    if str.isalpha(a):
        counter = counter + 1

    if str.isupper(a):
        b = GetCypherCharUpper(a, k[(counter % modLength)])

    elif str.islower(a):
        b = GetCypherCharLower(a,k[(counter % modLength)])
    
    c = int(b)
    print(f"{chr(c)}", end="")

print("")


exit


    
