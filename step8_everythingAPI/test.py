

#create a function for login function that takes two argumnets a username and password
#if the username and password are correct, return true, otherwise return false
def login(username, password):
    if username == 'admin' and password == 'password':
        return True
    else:
        return False
login('admin', 'passwor')


#create a function to register that takes two arguments username and password
#if the username is already taken, return false, otherwise return true
def register(username, password):
    if username == 'admin':
        return False
        
    else:
        return True
