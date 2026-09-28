from datetime import datetime, date
from persistent import Persistent 
from persistent.list import PersistentList

class Distribution(Persistent):
    def __init__(self, org, date, type, pax):
        self.org = org
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.type = type
        self.pax = pax

    def __repr__(self):
        return (f"[Organisation: {self.org}, Date: {self.date}, Type: {self.type}, Number of People: {self.pax}]")

class Block(Persistent):
    def __init__(self, block, postcode):
        self.block = block
        self.postcode = postcode
        self.latest_distribution = None
        self.past_distributions = PersistentList()

    def log_distribution(self, distribution):
        if self.latest_distribution is not None:
            self.past_distributions.append(self.latest_distribution)

        self.latest_distribution = distribution

    def display_distributions(self):
        if self.latest_distribution == None:
            print("No Record")
            return

        print(f"Food Distribution Records of Block {self.block}")
        for i in range(len(self.past_distributions)):
            print(self.past_distributions[i].__repr__())
        
        print(self.latest_distribution.__repr__())

    def time_since_last_distribution(self):
        if self.latest_distribution == None:
            return "No Record"

        return (date.today() - self.latest_distribution.date).days

    def __repr__(self):
        if self.latest_distribution is None:
            ld = "No Record"
        else:
            ld = self.latest_distribution.__repr__()

        return(f"[Block: {self.block}, Postal Code: {self.postcode}, Latest Distribution: {ld}, Days Since Latest Distribution: {self.time_since_last_distribution()}, Number of Previous Distributions: {len(self.past_distributions)}]")

class Neighbourhood(Persistent):
    def __init__(self, name, blocks):
        self.name = name
        self.blocks = PersistentList(blocks)

    def display_blocks(self):
        print(f"Blocks in {self.name}")
        for i in range(len(self.blocks)):
            print(self.blocks[i])
