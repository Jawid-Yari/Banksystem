import datetime 
import random
from time import perf_counter
from barnum import gen_data
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
            start = perf_counter()
            result =func(*args, **kwargs)
            end = perf_counter()
            print( f"{message} took {end - start} seconds")
            return result
        return inner
    return decorator
    



class Customer_database: 
    def __init__(self):
        self.customers = []
        self.generated_account_number = set()

    def __repr__(self) -> str:
        return self.customers
    
    def quicksort(self, customers):
        if len(customers) <= 1:
            return customers
        else:
            pivot = customers[0].account_number[-10:]
            smaller = [customer for customer in customers if customer.account_number[-10:] < pivot]
            equal = [customer for customer in customers if customer.account_number[-10:] == pivot]
            larger = [customer for customer in customers if customer.account_number[-10:] > pivot]
            return self.quicksort(smaller) + equal + self.quicksort(larger)

    
    def sort_customers_by_account_number(self):
        self.customers = self.quicksort(self.customers)


    @count_time("Searching for account number")
    def binary_search(self, element):
        lista_of_account_numbers = [customer.account_number[-10:] for customer in self.customers]
        number_to_search = element[-10:]
        length = len(lista_of_account_numbers)-1
        low = 0
        while low <= length:
            medium = (low + length)//2
            if number_to_search < lista_of_account_numbers[medium]:
                length = medium -1 
            elif number_to_search > lista_of_account_numbers[medium]:
                low = medium + 1
            elif number_to_search == lista_of_account_numbers[medium]:
                print(f"Account number '{element}' matchar {lista_of_account_numbers[medium]}")
                break
    

    def generate_account_num(self, c):
        account_number = f"1111-{c:00000000010}"
        return account_number
        


    def last_updated_time(self) -> datetime:
        return datetime.datetime.now()
        

    def generate_customer(self,number_of_customer):
        
        for _ in range(1, number_of_customer + 1):
            name = ''.join(gen_data.create_name())
            birthdate = gen_data.create_birthday()
            account_number = self.generate_account_num(_)
            created = gen_data.create_date()
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
    customer_db.generate_customer(100)



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

    accounts_to_check = ["1111-0000001000", "1111-0009999999", "1111-9999999999"]
    for item in (accounts_to_check):
        customer_db.binary_search(item)

    
    for customer in customer_db.customers:
        print(customer)
    
