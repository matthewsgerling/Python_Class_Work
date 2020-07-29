class CSVreader:

    def __init__(self, county, capitalincome, householdincome, familyincome, population, num_households):
        self.population = population
        self.num_households = num_households
        self.capitalincome = capitalincome
        self.householdincome = householdincome
        self.familyincome = familyincome
        self.county = county
