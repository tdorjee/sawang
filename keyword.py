file = open("rockyou.txt", "r", errors="ignore")

def is_camel_case(s):
    return s != s.lower() and s != s.upper() and "_" not in s

## User to enter a keyword
keyword = input("Enter a text: ")

## keyword matching passwords will be appending in this array
keywordMached = []

## Iterate over the all the passwords in rockyou.txt against the keyword to check if either keyword maches a password 
## or keyword is a substring of a password. If true, append passwords to keywordMached array.

for eachPassword in file:

    cleanEachPassword = eachPassword.strip()
    
    if cleanEachPassword.isupper():
        lowerCasedPassword = cleanEachPassword.lower()
        if keyword in lowerCasedPassword:
            keywordMached.append(eachPassword.strip())
    elif is_camel_case(cleanEachPassword):
        lowerCasedPassword = cleanEachPassword.lower()
        if keyword in lowerCasedPassword:
            keywordMached.append(eachPassword.strip())
    else:
        if keyword in cleanEachPassword:
            keywordMached.append(eachPassword.strip())

## Display all the the matching passwords and passswords containing a keyword as a substring

print(keywordMached)

file.close()