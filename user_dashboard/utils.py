import random


def generate_account_number():
    account_number = ''.join(str(random.randint(0, 9)) for _ in range(10))
    return account_number
