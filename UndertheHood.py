from functools import total_ordering

import pandas
from numpy.core.multiarray import item
from numpy.ma.core import masked
from pandas.core.methods.describe import select_describe_func


class UnderTheHood:

    def __init__(self,data):
        self.data = pandas.read_csv(data)

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
        # gets total amount of items
        total = len(self.data)
        series = self.genretotalcounter()
        averages = []
        # gets % average for all movies
        for newitem in series.index:
            averages.append(newitem/total)

        # turns it into panda series and sorts it from least->most genre%
        return pandas.Series(series.values, index=averages).sort_index()

    def sortbylessthan(self, budget):
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
# todo: why... not work?
    def sortbyyears(self,startyear,endyear):
        masked = pandas.to_numeric(self.data["ReleaseDate"], errors="coerce").le(startyear)
        return self.data[masked].reset_index(drop=True)

#doesn't work so fix sortbylessthan