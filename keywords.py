file = open("rockyou.txt", "r", errors="ignore")

def is_camel_case(s):
    return s != s.lower() and s != s.upper() and "_" not in s

## Add as many keyword as you'd like in keywords array 
keywords = ["keywordOne", "keywordTwo"] 

## keyword matching passwords will be appending in this array
keywordMached = []

## Iterate over the all the passwords in rockyou.txt for each keyword to check if either keyword maches a password 
## or keyword is a substring of a password. If true, append passwords to keywordMached array.

for eachPassword in file:
    
    cleanEachPassword = eachPassword.strip()

    if cleanEachPassword.isupper():
        lowerCasedPassword = cleanEachPassword.lower()
        for eachKeyWord in keywords:
            if eachKeyWord in lowerCasedPassword:
                keywordMached.append(eachPassword.strip())
    elif is_camel_case(cleanEachPassword):
        lowerCasedPassword = cleanEachPassword.lower()
        for eachKeyWord in keywords:
            if eachKeyWord in lowerCasedPassword:
                keywordMached.append(eachPassword.strip())
    else:
        lowerCasedPassword = cleanEachPassword.lower()
        for eachKeyWord in keywords:
            if eachKeyWord in lowerCasedPassword:
                keywordMached.append(eachPassword.strip())

## Display all the the matching passwords and passswords containing a keyword as a substring

print(keywordMached)

file.close()
