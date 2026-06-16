# MovieTrendAnalytics
A personal project where I'll use data science and programming to discover genre trends between indie and major film studios

If you are using, be sure to extract the dataset from the zip file. then run main.py
## Plan
1. Find source for data
   1. what is the differnce between a big/small budget film?
2. Plan out what program will look like
   1. Coding files
   2. (optional) front end
3. Writing the actual code
4. Document results
## Completed parts of plan
1. Find source for data
   I have decided to use [Kaggle's dataset of movie](https://www.kaggle.com/datasets/mjshubham21/movie-dataset-for-analytics-and-visualization?resource=download), as it has adequate movie data for it and is the easiest to use without sacfricing data accuracy
2. coded in python, does exactly what is requested
3. see above
   1. I think some front end would be nice. Just a nice visualizer.
### 5/12/26
   not much today tbh. downloaded the data set, tested it out a bit, and yeah. now I gotta learn panda but it should be fun
   
### 5/14/26
   learned the syntax a bit, however I realized that the data set is huge. so I should just test it with the first 5 vairables before moving on to testing the whole thing. Also began organzing a bit now that I know what I'm doing
   
### 5/15/26
   further progress on functions and genre collection
### 5/18/26
   simplifed the code. UndertheHood now takes one data object and all classes intereact with that single instance. Added average finder
### 5/20/26
   Found out a better way to do alot of things. Alot of code rewritten.
### 5/26/26
   Got pretty much everything I want from it: shows genre popularity when given anything less than a certain budget.
### 5/27/26
   Added piechart for visulazation purposes
### 6/02/26
   should now be good for anyone to use. Realized that gotta make it sort by income above certain threshold so that indie films aren't included in the major films
   prooveing a bit more diffuclt than what i once though. Trying to do a area graph to make it easier to see the progression and decline. but keeps not showing incorrect output
   did some bug testing, and maybe there isn't any substianl genre trends at all? at least in terms of what is being made in the indie genre
   will test it with how much money each genre made over the decades. I looked at other data sets and I believe something is worng in mine with how i counted the data. the genreaverage() could be the culprit
### 6/03/26   
   after some research and quick math, I've come to the conclsion that the data output is right. Which is intresting, because it shows no major genre intrest change
   refineded the over decades genre trends. Started work on revune earned by genres too.
### 6/04/26
   Had to do alot of googling and research to figure out how sort genres by earnings. Eairler worked fine since was just one collumn, now however things are a bit different
   but i got it working. IS very slow, and I need to find a faster and better way to do it, but for now it gets job done.
   I can use the new function to get movies from a decade and see what sold well back then too.
### 6/06/26
   Simplifed genre counter
   Worked on way to see genre consumer popualirty. Still, something doesn't seem right. Results show no major changes at all.
   thinking about switching to another dataset, maybe TMDB? Results are baffaling, and upon looking at documentary movies it should show that they rise in popualiryty entering the 2000s.
   Most of the code is built off the CSV, so if I were to move to TMDB I'd have to use the API to convert the data into a CSV
   which is pretty unlikely ngl. So I'd have to rewrite the code.
   but what other choice do I have? 
   I'll change my dataset to TMDB once I am for certain that all my code works for this current dataset. As in, does everything I'd want it to do for the other as well.
### 6/08/26
   Started working on the TMDB API, first time using any API but so far I got it to give me a list of all genres. Now just need it to extract the list of all movies...
   Gonna use a Go file for the API since it is the fastest and I need speed for this. Esepcailly considering the amount of data. Will only use the API once, but the genre i still would like to directly plug intp python as best as i can
### 6/09/26
   TMDB doesn't have documenation for extracting just budget but am working through it
### 6/09/26
   TMDB dataset intergeated mostly. Alot of the data I gathered lacks budget and boxoffice, however the small portion that does is sufficent
### 6/15/26
    I have begun the data anaylis of all the data. Will have to write code to see proffitablity of genres too however