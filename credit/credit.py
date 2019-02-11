letter= "Z"


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



print(f"{upperToLower(letter)}")