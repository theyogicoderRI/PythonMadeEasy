import string
import secrets

##Generate a 12-character alphanumeric password with at least one lowercase character,
##at least one uppercase character, special characters and at least 1 number.

alphabet = string.ascii_letters + string.digits + string.punctuation
x =string.punctuation
while True: 
    password = ''.join(secrets.choice(alphabet) for i in range(12))
    
    if (any(c.islower() for c in password) and
        any(c.isupper() for c in password)  
        and sum(c.isdigit() for c in password) >= 1 ):
            
        print(password) 
        break


##import secrets
##import string
##stringSource  = string.ascii_letters + string.digits + string.punctuation
##password = secrets.choice(string.ascii_lowercase)
##password += secrets.choice(string.ascii_uppercase)
##password += secrets.choice(string.digits)
##password += secrets.choice(string.punctuation)
##for i in range(12):
##    password += secrets.choice(stringSource)
##charList = list(password)
##secrets.SystemRandom().shuffle(charList)
##password = ''.join(charList)
##print ("Secure Password: ", password)
##
