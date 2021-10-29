def verify_pin(pin):
    if pin == 2684:
        return True
    else:
        return
# print(verify_pin(2684))

def log_in():
    count = 0
    while count < 3:
        pin = int(input('Enter PIN: '))
        if pin == 2684:
            print('Correct PIN')
            return True
        else:
            print('Try again')
            count += 1
    return
# print(log_in())

def set_start_balance():
    successful_login = log_in()
    set_balance = None
    if successful_login:
        set_balance = 100
        print(f'Your current balance is: {set_balance}')
        return True
    else:
        return

# print(set_start_balance())

def run_atm(amount):
    successful_start_balance = set_start_balance()
    if successful_start_balance:
        set_balance = 100
        amount = float(input('Enter amount to be  withdrawn'))
        balance = set_balance - amount
        try:
            if balance < 0 or amount > balance:
                raise Exception

            balance = set_balance - amount
            print(f'Current balance is: {balance}')
        except:
            print('Withdrawal incomplete. Insufficient funds in your account.')
        else:
            print('Withdrawal complete.')
        finally:
            print('Thank you for using our service.')

    else:
        return
    return

print(run_atm(50))
