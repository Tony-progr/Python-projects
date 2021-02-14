import os
#open the file with the info and save it:
lf = open('login.txt', 'r')
username = lf.readline()
password = lf.readline()

#Get only the wanted info from the file:
username = username.replace('Username:', '')
password = password.replace('Password:', '')

actual_username = username.strip()
actual_password = password.strip()

lf.close()

#Login check:
def login():

    #Get the user info:
    user_info = str(input('Password:'))

    #Check if the user info is correct:
    if user_info != actual_password:
        user_info = str(input('Wrong password! Try again:'))
        if user_info.strip() != actual_password:
            user_input = str(input('Wrong password. Did you forget it? (y/n)'))
            if user_input == 'y':
                lf = open('login.txt', 'w')
                new_password = str(input('New password:'))
                lf.write('Username: ' + username)
                lf.write('Password: '+ new_password)
                print('Password changed!')
                user_info = str(input('Login with new password:'))
                lf.close()
                if user_info != new_password:
                    print('Too many failed attemts...')
                    exit()
                elif user_info == new_password:
                    print('Login successful!')
            elif user_input == 'n':
                user_info = str(input('Password:'))
                if user_info == actual_password:
                    print('Login successful!')
                elif user_info != actual_password:
                    print('Too many failed attemts...')
                    exit()
            else:
                forgot_password_confirm = str(input('Wrong input please type yes or no! (y/n)'))
                if forgot_password_confirm == 'y':
                    lf = open('login.txt', 'w')
                    new_password = str(input('New password:'))
                    lf.write('Username: ' + username)
                    lf.write('Password: ' + new_password)
                    print('Password changed!')
                    user_info = str(input('Login with new password:'))
                    lf.close()
                    if user_info != new_password:
                        print('Too many failed attemts...')
                        exit()
                    elif user_info == new_password:
                        print('Login successful!')
                    else:
                        print('Unexpected error!')
                        exit()
                elif forgot_password_confirm == 'n':
                    user_info = str(input('Password:'))
                    if user_info == actual_password:
                        print('Login successful!')
                    elif user_info != actual_password:
                        print('Too many failed attemts...')
                        exit()
        elif user_info.strip() == actual_password:
            print('Login successful!')
        else:
            print('Unexpected error!')
            exit()
    elif user_info.strip() == actual_password:
        print('Login successful!')
    else:
        print('Unexpected error!')
        exit()

def password_manager():

    user_input = str(input('Do you want to add or view the login info for an app? (a/v)'))    

    if user_input == 'a':
        pf = open('passwords.txt', 'r')
        all_lines = pf.readlines()
        pf.close()

        app_name = str(input('Type the app\'s name:'))
        app_username = str(input('Type your username:'))
        app_password = str(input('Type you password:'))
        
        pf = open('passwords.txt', 'w')

        #Check if app allready exists:
        if app_name in str(all_lines):
            alrd_in = str(input('This app has allready been added. Do you want to change the info? (y/n)'))
            if alrd_in == 'y':
                new_app_username = str(input('Type the new username:'))
                new_app_password = str(input('Type the new password:'))

                for line in all_lines:
                    if app_username in line:
                        pf.write(line.replace(app_username, new_app_username))
                        if app_username in line:
                            pf.write(line.replace(app_password, new_app_password))
                            if app_name in line:
                                pf.write(line)
            elif alrd_in == 'n':
                print('Okay')
                exit()
            else:
                print('Unexpected error!')
                exit()
        elif app_name not in str(all_lines):
            for line in all_lines:
                pf.write(line)
        
            pf.write('\n')
            pf.write('\n')
            pf.write('App name: ' + app_name + '\n')
            pf.write(app_name + ' username: ' + app_username + '\n')
            pf.write(app_name + ' password: ' + app_password)
        else:
            print('Unexpected error!')
            exit()    

        print('Info saved!')
        exit()

    elif user_input == 'v':
        pf = open('passwords.txt', 'r')
        all_lines = pf.readlines()
        pf.close()

        if os.stat("passwords.txt").st_size > 0:
            app_view_name = str(input('Type the name of the app that you want to view!'))
            for line in all_lines:
                if app_view_name in line:
                    print(line)
            exit()
        elif os.stat("passwords.txt").st_size == 0:
            empty_msg = str(input('There is no saved info! Do you want to add some? (y/n)'))
            if empty_msg == 'y':
                pf = open('passwords.txt', 'r')
                all_lines = pf.readlines()
                pf.close()

                app_name = str(input('Type the app\'s name:'))
                app_username = str(input('Type your username:'))
                app_password = str(input('Type you password:'))
                
                pf = open('passwords.txt', 'w')

                #Check if app allready exists:
                if app_name in str(all_lines):
                    alrd_in = str(input('This app has allready been added. Do you want to change the info? (y/n)'))
                    if alrd_in == 'y':
                        new_app_username = str(input('Type the new username:'))
                        new_app_password = str(input('Type the new password:'))

                        for line in all_lines:
                            if app_username in line:
                                pf.write(line.replace(app_username, new_app_username))
                                if app_username in line:
                                    pf.write(line.replace(app_password, new_app_password))
                                    if app_name in line:
                                        pf.write(line)
                    elif alrd_in == 'n':
                        print('Okay')
                        exit()
                    else:
                        print('Unexpected error!')
                        exit()
                elif app_name not in str(all_lines):
                    for line in all_lines:
                        pf.write(line)
                
                    pf.write('\n')
                    pf.write('\n')
                    pf.write('App name: ' + app_name + '\n')
                    pf.write(app_name + ' username: ' + app_username + '\n')
                    pf.write(app_name + ' password: ' + app_password)
                else:
                    print('Unexpected error!')
                    exit()    

                print('Info saved!')
                exit()
            elif empty_msg == 'n':
                print('Okay!')
                exit()
            else:
                print('Unexpected error!')
                exit()
    else:
        print('Unexpected error!')
        exit()

login()
password_manager()