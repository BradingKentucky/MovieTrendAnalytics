# This is a sample Python script.
from functools import total_ordering
from random import choice
from tkinter import Scale

from pandas.core.computation.common import result_type_many


# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import pandas, UndertheHood

#following genres in the dataset: Action, Comedy, Documentary, Drama, Horror, Romance, Sci-Fi, Thriller

# prints data
    Testdata = UndertheHood.UnderTheHood("Test.csv")
   # Testdata = UndertheHood.UnderTheHood("movies_Dataset.csv")


# prints movieID 3 from the data
   # print(Testdata.iloc[2])
   # print("now should get just the title")
   # print(Data.iloc[2]["Title"])
    #diesction
        # .iloc : selects rows/columnts by interger position


    def choices():
        print(f"what do you wanna do?")
        print(f"1: total genre count")
        print(f"2: average")
        print(f"3: films with less than 1,500,000")
        print(f"4: comedies with less than 1,500,000. Compared to all comedies")
        choice = "5"
        if choice == "1":
            print("total genre count")
        if choice == "1":
            GenreDict = Testdata.genretotalcounter()
            print(GenreDict)
        elif choice == "2":
            print("now should get the average")
            print(Testdata.genreaverage())
        elif choice == "3":
            print("all films with budget less than 1,500,000")
            print(Testdata.sortbylessthan(1500000))
        elif choice == "4":
            print("All comedy films made with less than 1,500,000")
            catalog1=Testdata.sortbylessthanandgenre(1500000,"Comedy")
            print(catalog1)
            print("Compared to total comedy movies...")
            collection3 = Testdata.genretotalcounter()
            # convert the series into a dict, then get the %
            newdict = collection3.to_dict()
            percent1 = len(catalog1)/newdict["Comedy"]
            print(f"there is a total of {newdict["Comedy"]} Comedies. Meaning out of all of them, only {percent1} were made with a budget of less than 1,500,000")
        elif choice == "5":
            print("all films made between 1970-1989")
            print(Testdata.sortbyyears(1970,1989))
        else:
            choices()

    choices()



    #ok cool it works probs... check again
    #now lets get the average genere

    # make intger for each genre, add 1 each time it pops up. then amount mentioned / total



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
