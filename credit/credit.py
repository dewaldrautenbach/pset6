letter= "p"


def lowerToUpper(letter):
    if str.islower(letter):
        hex = ord(letter)
        upperCase = chr(hex-32)
        #print(f"{upperCase}")
        #print(f"{chr(hex-32)}")
        return upperCase
    else:
        return letter




print(f"{lowerToUpper(letter)}")