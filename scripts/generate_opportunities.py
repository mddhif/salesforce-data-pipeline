from faker import Faker
import csv
import random
from datetime import datetime, timedelta

fake = Faker()

stages = ["Prospecting", "Qualification", "Proposal", "Negotiation", "Closed Won", "Closed Lost"]

with open("opportunities.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Opportunity Name", "Account Name", "Amount", "Stage", "Close Date"])
    
    for _ in range(300):
        opp_name = f"{fake.bs().title()} Deal"
        account = fake.company()
        amount = round(random.uniform(500, 20000), 2)
        stage = random.choice(stages)
        close_date = (datetime.now() - timedelta(days=random.randint(0, 60))).strftime("%Y-%m-%d")
        writer.writerow([opp_name, account, amount, stage, close_date])
