from functools import total_ordering

import pandas
from numpy.core.multiarray import item
from numpy.ma.core import masked
from pandas.core.methods.describe import select_describe_func


class UnderTheHood:

    def __init__(self,data):
        self.data = data

    def genretotalcounter(self):
        Genres = ["Action", "Comedy", "Documentary", "Drama", "Horror", "Romance", "Sci-Fi", "Thriller"]
        Aca = 0
        Coa = 0
        Doa = 0
        Dra = 0
        Hoa = 0
        Roa = 0
        Sca = 0
        Tha = 0

        # todo: find better way to write above
        for item in self.data["Genre"]:
            if item == "Action":
                Aca = Aca + 1
            if item == "Comedy":
                Coa = Coa + 1
            if item == "Documentary":
                Doa = Doa + 1
            if item == "Drama":
                Dra = Dra + 1
            if item == "Horror":
                Hoa = Hoa + 1
            if item == "Romance":
                Roa = Roa + 1
            if item == "Sci-Fi":
                Sca = Sca + 1
            if item == "Thriller":
                Tha = Tha + 1
        Total = [Aca, Coa, Doa, Dra, Hoa, Roa, Sca, Tha]

        #makes a panda series, think of it as a dict but better
        return pandas.Series(Total, index=Genres)


    def genreaverage(self):
        # gets the total
        total = len(self.data)
        # gets total generes
        series = self.genretotalcounter()
        #divides to get % and returns that as a dict
        return (series / total).to_dict()

        # turns it into panda series and sorts it from least->most genre%
        return pandas.Series(series.values, index=averages).sort_index()

    def sortbylessthan(self, budget):
        self.data.columns = self.data.columns.str.strip()
        mask = pandas.to_numeric(self.data["BudgetUSD"], errors="coerce").le(budget)
        return self.data[mask].reset_index(drop=True)

    def sortbylessthanandgenre(self, limit, genre):
        df = self.data  # self.data is a DataFrame
        # makes boolean mask (anything that matches mask is selected)
        # numeric thing makes budget into float variables
        #.le is the less than or equal to comparsion
        mask = pandas.to_numeric(df['BudgetUSD'], errors='coerce').le(limit) & (df['Genre'] == genre)
        #df[mask] selects rows of self.data where mask is true.
        # reset_index returns the cleaned filtered data
        return df[mask].reset_index(drop=True)

    def sortbyyears(self,startyear,endyear):
        #gets the data from the self.data and males ReleaseYear the searcahble thing
        masked = pandas.to_numeric(self.data["ReleaseYear"], errors="coerce")
        #filters by greater than or equal to and vice versa
        masked2 = masked.ge(startyear) & masked.le(endyear)
        #returns it all
        return self.data[masked2].reset_index(drop=True)

    def sortbyyearsandgenre(self,startyear,endyear,genre):
        step1=self.sortbyyears(startyear,endyear)


#doesn't work so fix sortbylessthan