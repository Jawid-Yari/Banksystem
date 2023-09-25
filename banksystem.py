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

    
    def partition(self, list, start, end):
        pivot = list[start].account_number[-10:]
        low = start +1
        high = end
        while True:

            while low <= high and list[high].account_number[-10:] >= pivot:
                high = high -1
            while low <= high and list[low].account_number[-10:] <= pivot:
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
    

    @count_time("to sort customers")
    def sort_customers_by_account_number(self):
        customers_list = self.customers
        self.quick_sort(customers_list, 0, len(customers_list) - 1)
        self.customers = customers_list


    def generate_names(slef) -> str:
        name = " ".join(gen_data.create_name())
        return name
    
    """
    while generating account numbers, verifying that there  is no dublicate account number genrated
    """
    def generate_account_num(self):
        while True:
            clearing_num = random.randint(1111,9999)
            account_num = random.randint(0, 9999999999)
            account_number = f"{clearing_num:04}-{account_num:010}"
            if account_number not in self.generated_account_number:
                self.generated_account_number.add(account_number)
                return account_number

    

    def last_updated_time(self) -> datetime:
        return datetime.datetime.now()
        

    def generate_customer(self,number_of_customer):
        
        for _ in range(1, number_of_customer + 1):
            name = self.generate_names()
            birthdate = gen_data.create_birthday()
            account_number = self.generate_account_num()
            created = datetime.datetime.now()
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


@count_time("to create customers")
def generate_customers():
    customer_db.generate_customer(10_000_000)



@count_time("to search")    
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
   

    # for ac in customer_db.customers:
    #     print(ac)
