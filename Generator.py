def my_generator(n):
    value = 0 

    while value < n :
        yield value

        value += 1 


generator = my_generator(10)
for value in my_generator(5):
    print(value)

print(next(generator))
print(next(generator))
print(next(generator))


square_generator = (i * i for i in range(10))
print('square_generator : ',  square_generator)
for i in square_generator:
    print('Value of i : ', i)


def powTwoGen(max = 0):
    n = 0 
    while n < max:
        yield 2**n
        n += 1

print('power of 2 to 4 is :' )
for i in powTwoGen(14):
    print(i)

def all_even():
    n = 0 
    while True:
        yield n 
        n += 10000000

# for i in all_even():
#     print(i)

        
print('--------------------------------------------------')
def fibonacci_number(nums):
    x,y = 0,1
    for _ in range(nums):
        x,y = y , x+y
        yield x

def sqr_fibo_num(nums):
    for num in nums:
        yield num**2
        
fibonacci_number(10)

print('sum of the fibonacci number 10 is : ', sum(fibonacci_number(10)))
print('square of the fibonacci number 10 is : ', sum(sqr_fibo_num(fibonacci_number(10))))

print('--------------------------------------------------')
print('---------------------2-----------------------------')

import csv
from io import StringIO


LOAN_APPLICATIONS = """name,ssn,loan_amount
John Doe,000-00-0000,43200
Jane Doe,111-11-1111,7200
Jim Doe,222-22-2222,52800
Jane Doe,111-11-1111,390000
"""

def extract():
    with StringIO(LOAN_APPLICATIONS) as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row


CREDIT_REPORTS = {
    ("Jane Doe", "111-11-1111"): {
        "credit_score": 733,
        "credit_entries": [
            { "amount": 133000, "late_payment": False },
            { "amount": 10000, "late_payment": False }
        ]
    },
    ("John Doe", "000-00-0000"): {
        "credit_score": 692,
        "credit_entries": [
            { "amount": 232000, "late_payment": True },
            { "amount": 50000, "late_payment": False }
        ]
    }
}



print('--------------------------------------------------')
print('---------------------3-----------------------------')
print(CREDIT_REPORTS.get(('John Doe', '000-00-0000')))


#   total_credit_amount = sum(entry['amount'] for entry in credit_report['credit_entries'])
credit_report = CREDIT_REPORTS.get(('John Doe', '000-00-0000'))
total_amount =  sum(entry['amount'] for entry in credit_report['credit_entries'])
late_pament =  any(entry['late_payment'] for entry in credit_report['credit_entries'])
print('Total credit of john Doe : ', total_amount)
print('Is any late payment of  of john Doe : ', late_pament)
print('Credit score of John Doe : ',credit_report['credit_score'] )

new_entry =  { "amount": 232000, "late_payment": True }
CREDIT_REPORTS[("John Doe", "000-00-0000")]["credit_entries"].append(new_entry)
print(CREDIT_REPORTS)


# total_credit_amount = sum(entry['amount'] for entry in credit_report['credit_entries'])


       
            
