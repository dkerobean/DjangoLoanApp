import random
import secrets

def generate_account_number():
    
    account_number = ''.join(str(random.randint(0, 9)) for _ in range(10))
    return account_number

def generate_reference():
    
    return secrets.token_hex(16)
