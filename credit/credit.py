from sys import argv


letter= "Z"
argv = ""

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

def GetCypherCharLower(c, key):
    end = 0;
    if (c >= 'a' and c <= 'z'):
        end=122

    if (isLowerChar(c) == true):
        newCharLower = c + (convertCase(key))
    else:
        newCharLower = 0
        
        #while (newCharLower > end)
        #newCharLower -= 26;
        #return (char)newCharLower;



def GetCypherCharUpper(d, key):
    end = 0
    if (d >= 'A' and d <= 'Z'):
        end=90
    if (isUpperChar(d)==true):
        newCharUpper = d + (convertCase(key))
    else:
        return 0

        while True: 
            if newCharUpper > end:
                newCharUpper -= 26
                #return (char)newCharUpper;
                return newCharUpper
            break


#def main()

if (len(argv) < 1):
    print("Fatal Error - No arguments passed! Program will now terminate!")
    exit
else:
    (len(argv) > 0:
        lengthInput = len(argv[0])
        for a in range(lengthInput):
            if str.isalpha(argv[0][a])==0:
                print("error")
            else:
            print("Good")














#for(int a=0;  a < lengthInput; a++)
#    {
#        if( isalpha(argv[1][a]) == 0 )
#            {
#                printf("Error - Key entry invalid (Only characters allowed). The program will now terminate\n");
#                return 1;
#            }

#        else if(argc > 2)
#            {
#                printf("Error! Only a single word key allowed. Program will now terminate\n");
#                return 1;
#            }

#    }

#    char* k = (argv[1]);

#    string i = get_string("plaintext: ");
#    int length = strlen(i);
#    int modLength = strlen(k);

#    printf("ciphertext: ");

#    char p;
#    char q;

#    int counter = -1;

#    for (int n = 0; n < length; n++)
#        {

#            char a = i[n];

#            if (isalpha(a))
#            {
#                counter=counter+1;
#            }

#            if (isupper(a))
#            {
#                a = GetCypherCharUpper(a,k[(counter % modLength)]);
#            }

#            else if(islower(a))
#            {
#                a = GetCypherCharLower(a,k[(counter % modLength)]);
#            }

#        printf("%c", a);
#    }



#    printf("\n");
#     return 0;
#}
