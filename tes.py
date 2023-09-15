from faker import Faker
from time import time
import datetime
class Customer:
    def __init__(self, name, birthdate, account_number, created,saldo, last_updated: str = None):
        self.name = name 
        self.birthdate = birthdate
        self.account_number = account_number
        self.created = created
        self.saldo = saldo
        self.last_updated = last_updated

    def __repr__(self) -> str:
        return (f"Account Owner: {self.name}\n"
                f"Birthdate: {self.birthdate}\n"
                f"Account number: {self.account_number}\n"
                f"Created date: {self.created}\n"
                f"Saldo: {self.saldo}\n"
                f"Last updated: {self.last_updated}\n"
                )

def generate_account_num(c):
        account_number = f"1111-{c:00000000010}"
        return account_number

customers = {}
for c in range(1, 10):
            fake = Faker()
            name = "Ali"
            birthdate = datetime.datetime.now()
            account_number = generate_account_num(c)
            created = datetime.datetime.now()
            saldo = 100000
            last_updated = datetime.datetime.now()
            customer = Customer(name=name, birthdate=birthdate,
                                account_number=account_number, 
                                created=created, saldo=saldo,
                                last_updated= last_updated 
                                )
            customers[account_number] = customer

print(customers.keys)