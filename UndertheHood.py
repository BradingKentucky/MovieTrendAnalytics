from functools import total_ordering

import pandas
from numpy.core.multiarray import item
from numpy.ma.core import masked
from pandas.core.methods.describe import select_describe_func


class UnderTheHood:

    def __init__(self,data):
        self.data = data

    def genretotalcounter(self):
        Genres = {'Action': 0, 'Comedy': 0, 'Documentary': 0, 'Drama': 0, 'Horror': 0, 'Romance': 0, 'Sci-Fi': 0, 'Thriller': 0}

        # done: find better way to write above
        for item in self.data["Genre"]:
            for genre in Genres:
                if item == genre:
                    Genres[item] += 1

        #makes a panda series, think of it as a dict but better
        return pandas.Series(Genres, index=Genres)


    def genreaverage(self):
        # gets the total
        total = len(self.data)
        # gets total generes
        series = self.genretotalcounter()
        #divides to get % and returns that as a dict

        # possible error here? maybe it doesn't divied each genere count by the total series?
        # but instead divided the entire genre count by total films?
        # fix would be for loop for each genre
        # no it does it right
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

        # do know that this turned it into a single collumn as well, which lets the next line of code work
        masked = pandas.to_numeric(self.data["ReleaseYear"], errors="coerce")
        #filters by greater than or equal to and vice versa
        masked2 = masked.ge(startyear) & masked.le(endyear)
        #returns it all
        return self.data[masked2].reset_index(drop=True)

    def sortbyyearsandgenre(self,startyear,endyear,genre):
        step1=self.sortbyyears(startyear,endyear)

    def sortbyyearsandmoney(self, startyear, endyear, budget,TrueforBelow):
        # this keeps the whole dataset intact (unlike other one).
        newdata = self.data[(self.data['ReleaseYear'] >= startyear) & (self.data['ReleaseYear'] <= endyear)]

        # Filter by budget and sort
        if TrueforBelow:
            newdata = newdata[newdata['BudgetUSD'] <= budget]
            newdata = newdata.sort_values(by=['BudgetUSD'], ascending=False)
            # then get genre count so you only get the genre count, makes data cleaner.

        elif not TrueforBelow:
            newdata = newdata[newdata['BudgetUSD'] > budget]
            newdata = newdata.sort_values(by=['BudgetUSD'], ascending=False)
        return newdata


        #newset = self.sortbyyears(int(startyear), int(endyear))
        #datapt1 = UndertheHood.UnderTheHood(newset)
        #return(self.sortbylessthan(budget))
        #datapt67 = UndertheHood.UnderTheHood(genrecount)
#doesn't work so fix sortbylessthan
    # keep rows where Worldwide (or whichever revenue column) >= timesbudget * BudgetUSD
    def sortbyearnings(self, timesbudget):
        profited = []
        for idx, row in self.data.iterrows():  # row is a Series
            product = pandas.to_numeric(row['BudgetUSD']) * timesbudget
            # do something with product, e.g. save
            if pandas.to_numeric(row['Global_BoxOfficeUSD']) >= pandas.to_numeric(product):
                profited.append(idx)
                # use idx not row. idx is entire row, while row is just "row 1" and doesn't include all
                # the data that you'd need

        return self.data.loc[profited]

