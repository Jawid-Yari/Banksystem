import datetime 
import random
from time import time
from faker import Faker
import string
class Customer:
    def __init__(self, name, birthdate, account_number, created,saldo, last_updated: str = None):
        self.name = name 
        self.birthdate = birthdate
        self.account_number = account_number
        self.created = created
        self.saldo = saldo
        self.last_updated = last_updated

    def __repr__(self) -> str:
        return (f"Account owner: {self.name}\n"
                f"Birthdate: {self.birthdate}\n"
                f"Account number: {self.account_number}\n"
                f"Created date: {self.created}\n"
                f"Saldo: {self.saldo}\n"
                f"Last Updated: {self.last_updated}\n"
                )



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
    



class Customer_database: 
    def __init__(self):
        self.customers = []
        self.generated_account_number = set()

    def __repr__(self) -> str:
        return self.customers

    def sort_account_number(self):
        for customer in self.customers:
            customer.account_number[-10]


    
    def quicksort(self, customers):
        if len(customers) <= 1:
            return customers
        else:
            pivot = customers[0].account_number[-10:]
            less_than_pivot = [customer for customer in customers[1:] if customer.account_number[-10:] < pivot]
            equal_to_pivot = [customer for customer in customers[1:] if customer.account_number[-10:] == pivot]
            greater_than_pivot = [customer for customer in customers[1:] if customer.account_number[-10:] > pivot]
            return self.quicksort(less_than_pivot) + equal_to_pivot + [customers[0]] + self.quicksort(greater_than_pivot)

    @count_time("sorting")
    def sort_customers_by_account_number(self):
        self.customers = self.quicksort(self.customers)


    def generate_names(slef) -> str:
        len_name = random.randint(3,8)
        first_letter = random.choice(string.ascii_uppercase)
        rest_of_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_name))
        name = first_letter + rest_of_string
        return name 
    

    def generate_account_num(self):
        while True:
            clearing_num = random.randint(1111,9999)
            account_num = random.randint(0, 9999999999)
            account_number = f"{clearing_num:04}-{account_num:010}"
            if account_number not in self.generated_account_number:
                self.generated_account_number.add(account_number)
                return account_number
        


    def generate_date(self):
        created = datetime.date(random.randint(1940, 2000), 
                                    random.randint(1, 12), 
                                    random.randint(1, 24))
        return created
    


    def last_updated_time(self) -> datetime:
        return datetime.datetime.now()
        

    def generate_customer(self,number_of_customer):
        
        for _ in range(1, number_of_customer + 1):
            name = self.generate_names()
            birthdate = self.generate_date()
            account_number = self.generate_account_num()
            created = self.generate_date()
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







if __name__ == "__main__":
    
    customer_db = Customer_database()
    generate_customers()

    customer_db.sort_customers_by_account_number()

    for ac in customer_db.customers:
        print(ac)
