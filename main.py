from datetime import date

import pandas as pd
import random
from faker import Faker


def random_person_data(num_records, domain_name, file_type):
    faker = Faker()

    first_names = [faker.first_name() for _ in range(num_records)]
    last_names = [faker.last_name() for _ in range(num_records)]
    middle_initials = [chr(random.randint(65, 90)) for _ in range(num_records)]
    dob = [faker.date_between_dates(date_start=date(1950, 1, 1), date_end=date(2004, 1, 1)) for _ in
           range(num_records)]
    phone_numbers = [faker.phone_number() for _ in range(num_records)]

    emails = [f"{first[:3].lower()}.{last.lower()}@{domain_name}" for first, last in
              zip(first_names, last_names)]

    ssns = [faker.ssn() for _ in range(num_records)]

    df = pd.DataFrame({
        'First Name': first_names,
        'Last Name': last_names,
        'Middle Initial': middle_initials,
        'DOB': dob,
        'Phone Number': phone_numbers,
        'Email': emails,
        'SSN': ssns
    })

    if file_type == "xlsx":
        df.to_excel('random_people.xlsx', index=False)
    elif file_type == "csv":
        df.to_csv('random_people.csv', index=False)
    else:
        print("Invalid file type specified")


# Usage
num_records = 100  # Number of records you want to generate
domain_name = "abdc.com"  # Domain name for email
file_type = "csv"  # or 'xlsx'

if __name__ == '__main__':
    random_person_data(num_records, domain_name, file_type)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
