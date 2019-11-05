def encrypt(str):
    a,j,n=122,0,int(input("Enter shift:"))
    if(str.isupper()):
        a=90
    for i in str:
        if (i == ' '):
            str = str + ' '
            j += 1
            continue
        if ((ord(i) + n % 26) > a):
            str = str[:j] + chr((ord(i) + n % 26) - 26) + str[j + 1:]
        else:
            str = str[:j] + chr((ord(i) + n % 26)) + str[j + 1:]
        j += 1
    print(str)

def decrypt(str):
    a,j,n=97,0,int(input("Enter shift:"))
    if(str.isupper()):
        a=65
    for i in str:
        if (i == ' '):
            str = str + ' '
            j += 1
            continue
        if ((ord(i) - n % 26) < a):
            str = str[:j] + chr((ord(i) - n % 26) + 26) + str[j + 1:]
        else:
            str = str[:j] + chr((ord(i) - n % 26)) + str[j + 1:]
        j += 1
    print(str)



str=input("Enter string:")
encrypt(str)
enc_str=input("Enter encrypted string:")
decrypt(enc_str)