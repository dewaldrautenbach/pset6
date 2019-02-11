from sys import argv

def isLowerChar(input):
    if str.islower(str(input)):
       return true
    else:
       return False

def isUpperChar(input):
    if str.isupper(str(input)):
       return true
    else:
       return False
   
def lowerToUpper(letter):
    if str.islower(letter):
        hex = ord(letter)
        upperCase = chr(hex-32)
        #print(f"{upperCase}")
        #print(f"{chr(hex-32)}")
        return upperCase
    else:
        return letter

def upperToLower(letter):
    if str.isupper(letter):
        hex = ord(letter)
        lowerCase = chr(hex+32)
        #print(f"{upperCase}")
        #print(f"{chr(hex-32)}")
        return lowerCase
    else:
        return letter

def convertCase(toConvert):
    if str.isupper(toConvert):
        output = ord(toConvert)-65
        print(f"{output}")
    else:
        output = ord(toConvert)-97
    return output


def GetCypherCharUpper(d, key):
    end = 0;
    if (d >= ord('A') and d <= ord('Z')):
        end=90;

    if (isUpperChar(d)==True):
        newCharUpper = d + (convertCase(key))
    else:
        return 0
    while True:
        if newCharUpper > end:
            newCharUpper -= 26
        else:
            break
    
        return newCharUpper


key = "z"
keyDigit=ord(key)

if keyDigit <= 90:
    keyMovement = keyDigit-65
    print(f"In scope: {keyMovement}")
    print(f"Key Digit: {keyDigit}")

if keyDigit > 90:
    print(f"Not in scope of uppercase: {keyDigit}")

print(f"Convert back to key: {chr(keyDigit)}")

keyDigit=ord(key)

if keyDigit >=97 and keyDigit <=122:
    keyMovement = keyDigit-97
    print(f"In scope of lowercase: {keyMovement}")
    print(f"Key Digit: {keyDigit}")

if keyDigit > 122:
    print(f"Not in scope: {keyDigit}")

print(f"Convert back to key: {chr(keyDigit)}")





#def GetCypherCharLower(c, key):
#    end = 0;
#    if (c >= ord('a') and c <= ord('z')):
#        end=122

#    if (isLowerChar(c) == True):
#        newCharLower = c + (convertCase(key))
#    else:
#        newCharLower = 0
#    while True:
#        if newCharLower > end: #wraparound of key... i.e. to stay between ascii a to z OR A to Z
#            newCharLower -= 26
#        else:
#            break
#    return newCharLower     
 


#def GetCypherCharUpper(d, key):
#    end = 0
#    if (d >= ord('A') and d <= ord('Z')):
#        end=90
#    if (isUpperChar(d) == True):
#        newCharUpper = d + +(convertCase(key))
#    else:
#        return 0

#        while True: 
#            if newCharUpper > end:
#                newCharUpper -= 26
#                return newCharUpper
#            break



##def main()

#if (len(argv) < 1):
#    print("Fatal Error - No arguments passed! Program will now terminate!")
#    exit
#if (len(argv) > 0):
#    lengthInput = len(argv[0])
#    for a in range(lengthInput):
#        if str.isalpha(argv[0][a])==0:
#            print("Error - Only Alphabetical Characters allowed")
       


#k = (argv[0]);

#i = "Dewald"
#length = len(i)
#modlength = len(k);

#print("ciphertext: ")

#counter = -1;


#for c in i:
#    if str.isalpha(c):
#        counter=counter+1

#    if str.isupper(c):
#        a = GetCypherCharUpper(a,k[(counter % modlength)])
#    elif str.islower(c):

#         a = GetCypherCharLower(a,k[(counter % modlength)]);
#    print(f"{a}")