import time

#default username a+ pass
user1 = 'user1'
pass1 = 'pass'

#lists for usernames and passwords
userbase = ['user1',]
passbase = ['pass1',]

#yes and no lists to compare with user responses
yes = ['Yes', 'yes', 'y', 'Y']
no = ['No', 'no', 'N', 'n']

#asks user if they have an account
newAcc = input('Welcome, do you have an account?')


if newAcc in yes:
    userReq = str(input('Please enter your username.')) #prompts user for their username
    passReq = str(input('Now please enter your password.')) #prompts user for password
    if userReq in userbase: #checks if user is in user list
        if passReq in passbase: #checks if the password user entered is in the password list
            print('Welcome to Monarch, ' + user1)
    else:
        print('Access Denied')
elif newAcc in no:
    create = input('Would you like to create a new account?') #prompts user if they would like to create a new accoumt
    if create in yes:
        pol = input('What username would you like?')
        list.append(userbase, pol) #assigns user's chosen username into userlist
        dab = input('Set the password you will use.')
        list.append(passbase,dab) #assigns user's chosen password into userlist






