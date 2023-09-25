from dataclasses import dataclass
import datetime 
import random
from time import time
from faker import Faker

@dataclass
class Customer:
    name: str
    birthdate:str 
    account_number: str 
    created: datetime
    saldo: float
    last_updated:datetime

    
    def __str__(self) -> str:
        formatted_output = (f"Account Owner: {self.name}\n"
                f"Birthdate: {self.birthdate}\n"
                f"Account number: {self.account_number}\n"
                f"Created date: {self.created}\n"
                f"Saldo: {self.saldo}\n"
                f"Last updated: {self.last_updated}\n"
                )
        return formatted_output



def count_time(message):
    def decorator(func:callable):
        def inner(*args, **kwargs):
            start = time()
            result =func(*args, **kwargs)
            end = time()
            print( f"{message} took {end - start} minutes")
            return result
        return inner
    return decorator
    


@dataclass
class Customer_database:  
    customers = []

    def __repr__(self) -> str:
        return self.customers
    

    def generate_names(slef) -> str:
        fake = Faker()
        name = fake.first_name()
        return name 
    

    def generate_account_num(self, c):
        account_number = f"1111-{c:00000000010}"
        return account_number


    def generate_created_date(self):
        created = datetime.date(random.randint(1940, 2000), 
                                    random.randint(1, 12), 
                                    random.randint(1, 24))
        return created
    


    def last_updated_time(self) -> datetime:
        return datetime.datetime.now()
        

    def generate_customer(self,number_of_customer):
        for c in range(1, number_of_customer + 1):
            fake = Faker()
            name = self.generate_names()
            birthdate = fake.date()
            account_number = self.generate_account_num(c)
            created = self.generate_created_date()
            saldo = random.uniform(0, 10000)
            last_updated = self.last_updated_time()
            customer = Customer(name=name, birthdate=birthdate,
                                account_number=account_number, 
                                created=created, saldo=saldo,
                                last_updated= last_updated 
                                )
            self.customers.append(customer)


    def get_account(self, account_to_search: str) -> Customer or None:
        for customer in self.customers:
            if customer.account_number == account_to_search:
                return customer
        return None








if __name__ == "__main__":
    
    customer_db = Customer_database()


    @count_time("Creating customer")
    def generate_customers():
        customer_db.generate_customer(10)


    @count_time("Searching")    
    def search_account(account_to_check: str):
        found_account = customer_db.get_account(account_to_search=account_to_check)
        if found_account:
            print(f"Account number {account_to_check} belongs to:'{found_account.name}' ")
        else:
            print(f"Account number: {account_to_check} not found")



    generate_customers()
    accounts_to_check = ["1111-0000001000", "1111-0009999999", "1111-9999999999"]
    for i in (accounts_to_check):
        search_account(i)