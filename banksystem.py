from dataclasses import dataclass
import datetime 
import random
from time import perf_counter
from barnum import gen_data



@dataclass
class Customer:
    name: str
    birthdate:str 
    account_number: str 
    created: datetime
    saldo: float
    last_updated:datetime


    """
    Jag vill formatera klassens output attribut
    """
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
            start = perf_counter()
            result =func(*args, **kwargs)
            end = perf_counter()
            print( f"It took {end - start} seconds {message}")
            return result
        return inner
    return decorator
    

@dataclass
class Customer_database: 
    customers = []
    generated_account_number = set()

    def __repr__(self) -> str:
        return self.customers
    
    def partition(self, list, start, end):
        pivot = int(list[start].account_number[-10:])
        low = start +1
        high = end
        while True:
            while low <= high and int(list[high].account_number[-10:]) >= pivot:
                high = high -1
            while low <= high and int(list[low].account_number[-10:]) <= pivot:
                low = low + 1 
            if low <= high:
                list[low], list[high] = list[high], list[low]
            else:
                break
        list[start], list[high] = list[high], list[start]

        return high
    
    
    def quick_sort(self, array, start, end):
        if start >= end:
            return
        p = self.partition(array, start, end)
        self.quick_sort(array, start, p-1)
        self.quick_sort(array, p+1, end)
    

    
    def sort_customers_by_account_number(self):
        customers_list = self.customers
        self.quick_sort(customers_list, 0, len(customers_list) - 1)
        self.customers = customers_list




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
                return(f"Account number '{element}' matchs {lista_of_account_numbers[medium]}")
                

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



@count_time("Creating customer")
def generate_customers():
    customer_db.generate_customer(10_000_000)



    
def search_account(account_to_check: str):
    for itam in account_to_check:
        found_account = customer_db.binary_search(element=itam)
        if found_account:
            print(found_account)
        else:
            print(f"Account number: {itam} not found")







if __name__ == "__main__":
    
    customer_db = Customer_database()
    generate_customers()

    customer_db.sort_customers_by_account_number()

    accounts_to_check = ["1111-0000001000", "1111-0009999999", "1111-9999999999"]
    search_account(account_to_check= accounts_to_check)

    
    for customer in customer_db.customers:
        print(customer)
    
