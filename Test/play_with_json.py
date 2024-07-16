## Get the total loan as of now 
## Get the total loan required 
## Check if credit_score > 700 then approve and add into the credit report with added in 20 pints in credit score


from io import StringIO
import csv
from typing import Generator, Dict, Any

LOAN_APPLICATIONS = """name,ssn,loan_amount
John Doe,000-00-0000,10000
Jane Doe,111-11-1111,12000
Jim Doe,222-22-2222,22000
Jane Doe,111-11-1111,10000
"""

CREDIT_REPORTS = {
    ("Jane Doe", "111-11-1111"): {
        "credit_score": 733,
        "credit_entries": [
            { "amount": 10000, "late_payment": False },
            { "amount": 10000, "late_payment": False }
        ]
    },
    ("John Doe", "000-00-0000"): {
        "credit_score": 692,
        "credit_entries": [
            { "amount": 10000, "late_payment": True },
            { "amount": 10000, "late_payment": False }
        ]
    }
}

class Extractor:
    def extract(self)-> Generator[Dict[str,Any], None, None]:
        with StringIO(LOAN_APPLICATIONS) as file:
            reader = csv.DictReader(file)
            for row in reader:
                yield row


class Transform:
    def transform(self,loan_data):
        print(loan_data)
        for data in loan_data:
            name, ssn = data['name'], data['ssn']
            credit_report = self._fetch_credit_report(name, ssn)
            # total_credit_amount = sum(entry['amount'] for entry in credit_report['credit_entries'])
            # # total_amount = credit_report['credit_entries']

            
    

    def _fetch_credit_report(self,name,ssn)-> Dict[str, Any]:
        data = CREDIT_REPORTS.get((name,ssn))
        print(data,{"credit_score":0,"credit_entries":[]} )
        return CREDIT_REPORTS.get((name,ssn),{"credit_score":0,"credit_entries":[]})
 

def main():
    extract = Extractor()
    transform = Transform()
    data = extract.extract()
    transform.transform(data)



main()