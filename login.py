
def signUp():
    username = input('Enter new username:   ')
    
    while True:
        password = input('Enter a new password: ')
        
        if len(password) < 8:
            print('Password must be of length greater than or equal to 8')
            continue
        else:
            has_upper = any(c.isupper() for c in password)
            has_lower = any(c.islower() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_special = any(c in ['@', '#', '&', '$'] for c in password)

            if has_upper and has_lower and has_digit and has_special:
                break
            else:
                print('Your password must satisfy the criteria:')
                if not has_upper:
                    print('- At least one uppercase alphabet (A - Z)')
                if not has_lower:
                    print('- At least one lowercase alphabet (a - z)')
                if not has_digit:
                    print('- At least one digit between 0 - 9')
                if not has_special:
                    print('- At least one of the special characters (@, #, &, $)')
    print('Account successfully created!')
signUp()
def logIn(username, password):
    pass

signUp()