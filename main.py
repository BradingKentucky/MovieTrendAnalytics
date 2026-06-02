# This is a sample Python script.
from _pyrepl.commands import end
from functools import total_ordering
from random import choice
from tkinter import Scale

from matplotlib.rcsetup import validate_int
from pandas.core.computation.common import result_type_many


# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import pandas, UndertheHood, matplotlib.pyplot as plt

#following genres in the dataset: Action, Comedy, Documentary, Drama, Horror, Romance, Sci-Fi, Thriller

# prints data
    newfile = pandas.read_csv("movies_dataset.csv")
    Testdata = UndertheHood.UnderTheHood(newfile)
   # Testdata = UndertheHood.UnderTheHood("movies_Dataset.csv")


# prints movieID 3 from the data
   # print(Testdata.iloc[2])
   # print("now should get just the title")
   # print(Data.iloc[2]["Title"])
    #diesction
        # .iloc : selects rows/columnts by interger position


    def choices():
        leave = True
        while leave:
            print(f"what do you wanna do?")
            print(f"1: total genre count")
            print(f"2: average")
            print(f"3: films with less than budget")
            print(f"4: a gener with less than budget. Compared to all in that genre")
            print(f"5:all films made between two years")
            print(f"6: See what genres were popualar between two years")
            print(f"7: See what genres were popualar between two years given that it be under a certain budget")
            print(f"0: Exit")
            choice = input("Choose option")
            if choice == "1":
                print("total genre count")
                GenreDict = Testdata.genretotalcounter()
                print(GenreDict)
            elif choice == "2":
                print("now should get the average")
                print(Testdata.genreaverage())
            elif choice == "3":
                years = input("max budget?")
                print(f"all films with budget less than {years}")
                print(Testdata.sortbylessthan(int(years)))
            elif choice == "4":
                print(f"Action:1, Comedy:2, Documentary:3, Drama:4, Horror:5, Romance:6")
                choice2 = input("genre choice?")
                valid = True
                while valid:
                    if choice2 == "1":
                        genre = "Action"
                        valid = False
                    elif choice2 == "2":
                        genre = "Comedy"
                        valid = False
                    elif choice2 == "3":
                        genre = "Documentary"
                        valid = False
                    elif choice2 == "4":
                        genre = "Drama"
                        valid = False
                    elif choice2 == "5":
                        genre = "Horror"
                        valid = False
                    elif choice2 == "6":
                        genre ="Romance"
                        valid = False
                    else:
                        choice2 = input("choose valid genre")

                budget = input("budget")

                print(f"All comedy films made with less than ${budget}")
                catalog1=Testdata.sortbylessthanandgenre(int(budget),genre)
                print(catalog1)
                print("Compared to total comedy movies...")
                collection3 = Testdata.genretotalcounter()
                # convert the series into a dict, then get the %
                newdict = collection3.to_dict()
                percent1 = len(catalog1)/newdict["Comedy"]
                print(f"there is a total of {newdict["Comedy"]} Comedies. Meaning out of all of them, only {percent1} were made with a budget of less than 1,500,000")
            elif choice == "5":
                startyear =int(input("start year?"))
                endyear = int(input("end year?"))
                print(f"all films made between {startyear}-{endyear}")
                print(Testdata.sortbyyears(startyear,endyear))
            elif choice == "6":
                startyear = int(input("Start year?"))
                endyear = int(input("End year?"))
                print(f"film genre average between {startyear} and {endyear}")
                twok = Testdata.sortbyyears(int(startyear),int(endyear))
                newdataset = UndertheHood.UnderTheHood(twok)
                newestset = pandas.Series(newdataset.genreaverage())
                newestset.plot(kind='pie',autopct='%1.1f%%')
                plt.title(f"Genre average from {startyear} to {endyear}")
                plt.show()

            elif choice == "7":
                startyear = input("Start year?")
                endyear = input("End year?")
                budget = int(input("Budget?"))
                newset = Testdata.sortbyyears(int(startyear),int(endyear))
                datapt1 = UndertheHood.UnderTheHood(newset)
                genrecount = datapt1.sortbylessthan(budget)
                datapt67 = UndertheHood.UnderTheHood(genrecount)
                average = pandas.Series(datapt67.genreaverage())
                average.plot(kind='pie',autopct='%1.1f%%')
                plt.title(f"Genre average from {startyear} to {endyear} under {budget}")
                plt.show()

            elif choice == "0":
                leave = False
                break
            else:
                choices()

    choices()



    #ok cool it works probs... check again
    #now lets get the average genere

    # make intger for each genre, add 1 each time it pops up. then amount mentioned / total



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
