# -- Defines the building blocks of the database, with objects Distribution, Block, and Neighbourhood -- 

from datetime import datetime, date
from zoneinfo import ZoneInfo

class Distribution():
    def __init__(self, org, date, type, pax, isHalal):
        self.org = org
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.type = type
        self.pax = pax
        self.isHalal = isHalal
        
    def __repr__(self):
        return (f"[Organisation: {self.org}, Date: {self.date}, Type: {self.type}, Number of People (Approx.): {self.pax}, Halal-Certified: {self.isHalal}]")

class Block():
    def __init__(self, block, postcode, coordinates):
        self.block = block
        self.postcode = postcode
        self.coordinates = coordinates
        self.latest_distribution = None
        self.distributions = {}
        self.deleted_distributions = []

    def log_distribution(self, dist_id, distribution): 
        self.distributions[dist_id] = distribution

        if (self.latest_distribution is None or distribution.date >= self.latest_distribution.date):
            self.latest_distribution = distribution

    def rem_distribution(self, dist_id):
        if dist_id not in self.distributions:
            return
        
        removed_dist = self.distributions.pop(dist_id)
        self.deleted_distributions.append(dist_id)
        
        if removed_dist == self.latest_distribution:
            if self.distributions:
                self.latest_distribution = max(self.distributions.values(), key = lambda dist : dist.date)
            else:
                self.latest_distribution = None

        return removed_dist
           
    def time_since_last_distribution(self):
        if not self.latest_distribution:
            return "No Record"
        return (datetime.now(ZoneInfo("Asia/Singapore")).date() - self.latest_distribution.date).days

    def __repr__(self):
        if not self.latest_distribution:
            ld = "No Record"
            pd = 0
        else:
            ld = self.latest_distribution.__repr__()
            pd = len(self.distributions) - 1

        return(f"[Block: {self.block}, Postal Code: {self.postcode}, Latest Distribution: {ld}, Days Since Latest Distribution: {self.time_since_last_distribution()}, Number of Previous Distributions: {pd}]")

class Neighbourhood():    
    def __init__(self, name, blocks):
        self.name = name
        self.blocks = blocks

    def __repr__(self):
        return(f"[Neighbourhood: {self.name}, Blocks: {[block.block for block in blocks]}]")