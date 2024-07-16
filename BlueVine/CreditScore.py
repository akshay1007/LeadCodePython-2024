import csv
from io import StringIO
from typing import Any, Dict, List, Generator

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
    def extract(self) -> Generator[Dict[str, Any], None, None]:
        with StringIO(LOAN_APPLICATIONS) as file:
            reader = csv.DictReader(file)
            for row in reader:
                yield row

class Transformer:
    def transform(self, loan_data: Generator[Dict[str, Any], None, None]) -> Generator[Dict[str, Any], None, None]:
        for loan in loan_data:
            name, ssn = loan['name'], loan['ssn']
            credit_report = self._fetch_credit_report(name, ssn)
            total_credit_amount = sum(entry['amount'] for entry in credit_report['credit_entries'])
            late_payment = any(entry['late_payment'] for entry in credit_report['credit_entries'])
            yield {
                "name": name,
                "ssn": ssn,
                "credit_score": credit_report['credit_score'],
                "total_credit_amount": total_credit_amount,
                "late_payment": late_payment
            }

    def _fetch_credit_report(self, name: str, ssn: str) -> Dict[str, Any]:
        return CREDIT_REPORTS.get((name, ssn), {"credit_score": 0, "credit_entries": []})

class Loader:
    def load(self, transformed_data: Generator[Dict[str, Any], None, None]) -> None:
        with StringIO() as file:
            output_fields = ['name', 'ssn', 'credit_score', 'total_credit_amount', 'late_payment']
            writer = csv.DictWriter(file, fieldnames=output_fields)
            writer.writeheader()
            for row in transformed_data:
                writer.writerow(row)
            print(file.getvalue())

def main():
    extractor = Extractor()
    transformer = Transformer()
    loader = Loader()

    loan_data = extractor.extract()
    transformed_data = transformer.transform(loan_data)
    loader.load(transformed_data)

main()
