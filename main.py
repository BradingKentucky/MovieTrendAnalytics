# This is a sample Python script.
from _pyrepl.commands import end
from functools import total_ordering
from operator import truediv
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
    import pandas, UndertheHood, matplotlib.pyplot as plt, subprocess as tmdb, json

#following genres in the base dataset: Action, Comedy, Documentary, Drama, Horror, Romance, Sci-Fi, Thriller
# in the tmdb, it is different. subproccess allows me to access that, self-explanatory
    GOoutput = tmdb.run(['go', 'run', 'TMDB_API.go'], capture_output=True, text=True,shell=True)
    # loads the outputted json string into Genres dict
    Genres = json.loads(GOoutput.stdout)
    # turns dict into list, every name (action) in the genres (whole dict) output
    Genres=[Genre['name'] for Genre in Genres['genres']]
    #print(Genres)
# prints data
    newfile = pandas.read_csv("movies_dataset.csv")
    Testdata = UndertheHood.UnderTheHood(newfile,Genres)
   # Testdata = UndertheHood.UnderTheHood("movies_Dataset.csv")


# prints movieID 3 from the data
   # print(Testdata.iloc[2])
   # print("now should get just the title")
   # print(Data.iloc[2]["Title"])
    #diesction
        # .iloc : selects rows/columnts by interger position
    def thing(threshold,BeloworNah):
        # thank you friend for coding this for me
        decade_starts = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
        if BeloworNah:
            title="under"
        elif not BeloworNah:
            title="above"

        # create variables data0..data9 as in your original naming
        processed = {}
        for i, start in enumerate(decade_starts):
            end = start + 9
            key = f"data{i}"  # creates data0..data8
            films = Testdata.sortbyyearsandmoney(start, end, threshold, BeloworNah)
            ut = UndertheHood.UnderTheHood(films)
            # genreaverage()return Series compatible)
            processed[f"data{i}"] = pandas.Series(ut.genreaverage())

        # Combine into DataFrame indexed by decade label, columns = genres
        decade_labels = [f"{s}s" for s in decade_starts]
        df = pandas.DataFrame([processed[f"data{i}"] for i in range(len(decade_starts))],
                              index=decade_labels).fillna(0)

        # Plot stacked area of genre composition by decade (counts or shares)
        # Optional: normalize per-decade to percent
        df_pct = df.div(df.sum(axis=1), axis=0) * 100

        ax = df_pct.plot(kind='area', stacked=True, figsize=(12, 6), colormap='tab20', alpha=0.85)
        ax.set_title(f"Genre share by decade ({title} ${threshold:,})")
        ax.set_xlabel("Decade")
        ax.set_ylabel("Percent")
        ax.legend(title="Genre", bbox_to_anchor=(1.02, 1), loc='upper left')
        plt.tight_layout()
        plt.show()

        # pie for the 1950s and onwards:
        for i in range(5):
            string = "data" + str(i)  # "decade5"
            ax = processed[string].plot(kind='pie', autopct='%1.1f%%')  # change index to appropriate data key
            plt.title(f"{decade_labels[i]} share of genres {title} ${threshold:,}")
            plt.ylabel("")
            plt.show()

        leave = False  # remove once done with dev

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
            print(f"8: view genre trends for films under a certain budget over 80 years (1950-2020)")
            print(f"9: view what was proffitable over the years for films under $5mill, only counting films that made 2.5* their budget")
            print(f"10: view generes from 1950-2026 that made X times their budget")
            print(f"0: Exit")
            input(choice)
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
                newdataset = UndertheHood.UnderTheHood(twok,Genres)
                newestset = pandas.Series(newdataset.genreaverage())
                newestset.plot(kind='pie',autopct='%1.1f%%')
                plt.title(f"Genre average from {startyear} to {endyear}")
                plt.show()

            elif choice == "7":
                startyear = input("Start year?")
                endyear = input("End year?")
                budget = int(input("Budget?"))
                newset = Testdata.sortbyyears(int(startyear),int(endyear))
                datapt1 = UndertheHood.UnderTheHood(newset,Genres)
                genrecount = datapt1.sortbylessthan(budget)
                datapt67 = UndertheHood.UnderTheHood(genrecount,Genres)
                average = pandas.Series(datapt67.genreaverage())
                average.plot(kind='pie',autopct='%1.1f%%')
                plt.title(f"Genre average from {startyear} to {endyear} under {budget}")
                plt.show()

            elif choice=="8":
                thing(5_000_000,True)
                thing(5_000_000,False)
                leave = False #remove once done with dev
            elif choice=="9":
                print("Working on it...")
                mostpopgenres2 = UndertheHood.UnderTheHood(Testdata.sortbyearnings(2.5))
                mostpopgenres3 = pandas.Series(mostpopgenres2.genreaverage())
                mostpopgenres3.plot(kind='pie',autopct='%1.1f%%')
                plt.title(f"most popular genres ever, by share that made 2.5* their budget")
                print("should now show chart")
                plt.show()
                #leave = False  # remove once done with dev
            elif choice=="10":
                reqment = input("how much money earned?")
                print(f"working on it...")
                decades = [(1950,1959),(1960,1969),(1970,1979),(1980,1989),(1990,1999),(2000,2009),(2010,2019),(2020,2029)]
                for start,end in decades:
                    decade_data = UndertheHood.UnderTheHood(Testdata.sortbyyears(int(start),int(end)))
                    count =decade_data.sortbyearnings(int(reqment))
                    if len(count) == 0:
                        print(f"no movie in this decade matches parameter, going to next decade")
                    else:
                        decade_data = UndertheHood.UnderTheHood(count)
                        pie_data = pandas.Series(decade_data.genreaverage())
                        pie_data.plot(kind='pie',autopct='%1.1f%%')
                        plt.title(f"% of movies in genres that made {reqment}* their budget, from {start}-{end}")
                        plt.show()

            elif choice=="11":
                budget = int(input("below what budget?"))
                reqment = input("how much money earned?")
                print(f"working on it...")
                decades = [(1950, 1959), (1960, 1969), (1970, 1979), (1980, 1989), (1990, 1999), (2000, 2009),
                           (2010, 2019), (2020, 2029)]
                for start, end in decades:
                    decade_data = UndertheHood.UnderTheHood(Testdata.sortbyyearsandmoney(int(start), int(end),budget,True))
                    count = decade_data.sortbyearnings(int(reqment))
                    if len(count) == 0:
                        print(f"no movie in this decade matches parameter, going to next decade")
                    else:
                        decade_data = UndertheHood.UnderTheHood(count)
                        pie_data = pandas.Series(decade_data.genreaverage())
                        pie_data.plot(kind='pie', autopct='%1.1f%%')
                        plt.title(f"% of movies made under {budget} in genres that made {reqment}* their budget, from {start}-{end}")
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
