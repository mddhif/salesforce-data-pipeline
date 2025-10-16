from faker import Faker
import csv
import random

fake = Faker()

# Possible Lead Status values
lead_statuses = ['Open - Not Contacted', 'Working - Contacted', 'Closed - Converted', 'Closed - Not Converted']

with open('leads.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Title', 'Company', 'Phone', 'Email', 'Lead Status'])
    
    for i in range(1, 101):  # Generate 100 leads
        name = fake.name()
        title = fake.job()
        company = fake.company()
        phone = fake.msisdn()[0:10]  # 10-digit phone
        email = fake.email()
        status = random.choice(lead_statuses)
        
        writer.writerow([name, title, company, phone, email, status])
