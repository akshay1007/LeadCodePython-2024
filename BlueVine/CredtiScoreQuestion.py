import csv
from io import StringIO
from typing import Any, Dict, List, Generator


LOAN_APPLICATIONS = """name,ssn,loan_amount
John Doe,000-00-0000,43200
Jane Doe,111-11-1111,7200
Jim Doe,222-22-2222,52800
Jane Doe,111-11-1111,390000
"""


CREDIT_REPORTS = {
    ("Jane Doe", "111-11-1111"): {
        "credit_score": 733,
        "credit_entries": [
            { "amount": 133000, "late_payment": False },
            { "amount": 10000,"late_payment": False }
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


class Extractor:

  # you can return normally instead of yielding if you prefer.
  def extract(self) -> Generator[Dict[str, Any], None, None]:
      with StringIO(LOAN_APPLICATIONS) as file:
          reader = csv.DictReader(file)
          for row in reader:
              yield row


class Transformer:

    def transform(self) -> Generator[Dict[str, Any], None, None]:
        # your solution here
        pass

    def _fetch_credit_report(self, name: str, ssn: str) -> Dict[str, Any]:
        # please integrate this according to your design.
        return CREDIT_REPORTS[(name, ssn)]


class Loader:

    def load(self) -> None:
        with StringIO() as file:
            output_fields = ['name', 'ssn', 'credit_score', 'total_credit_amount', 'late_payment']
            writer = csv.DictWriter(file, fieldnames=output_fields)
            writer.writeheader()
            # please integrate this according to your design.
            for row in ...:
                writer.writerow(row)


def main():
    # please put together a data pipeline out of the above classes.
    pass

main()