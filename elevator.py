import time

current_floor = 0

def elevate(user_floor):
    global current_floor
    while user_floor != current_floor: 
        current_floor += 1
        time.sleep(1)
        print(f'You are on floor no. {current_floor}')
    time.sleep(1)
    print('You are on the desired floor\n')

def depression(user_floor):
    global current_floor
    while user_floor != current_floor: 
        print(f'You are on floor no. {current_floor}')
        current_floor -= 1
        time.sleep(1)        
    time.sleep(1)
    print('You are on the desired floor\n')

def destination():
    while True:
        floor = int(input('Enter your desired floor between -2 to 10: '))
        if floor in range(-2, 11):
            break
        else:
            print('Enter a valid floor')
    return floor

def operate(user_floor):
    global current_floor
    if user_floor == current_floor:
        print('You are on the desired floor')
    elif user_floor > current_floor:
        elevate(user_floor)
    else:
        depression(user_floor)

user_floor = destination()
operate(user_floor)

while True:
    print('Do you want to continue or exit?')
    choice = input('Press E for exit or C for continue: ')
    if choice.upper() == 'E':
        print('Thank you for using our service')
        break
    elif choice.upper() == 'C':
        user_floor = destination()
        operate(user_floor)
    else:
        print('Enter a valid choice')
