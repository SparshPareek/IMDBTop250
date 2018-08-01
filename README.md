# IMDBTop250
This project fetches IMDB Top 250 Movie Names, Release Year and Rating.

Points to note : 
1. TestCase File is present in the Project itself named "IMDBTop250.xlsx"
2. Execute "IMDBTest.py" from command promt or any IDE after project import.

Project Features : 
1. This project incorporates Page Object Model("PageObject.py") and is built in Python Programming Language with Selenium to interact with the UI of IMDB.
2. It runs on Python Unittest Framework.

What it does : 
1. The project launches IMDB Top 250 Chart Page in Chrome Browser through Selenium and Python.
2. Checks whether the page that loads is the one intended.
3. It verifies that all the 250 Movie Links present on the Page are not broken with the help of "Requests" Module. If Broken it prints the broken link in console.
4. It fetches the Top 250 Movie Names, Release Year and Ratings from the page.
5. Stores the retrieved data into "Sqlite3" database named "IMDB250.db" present in the project directory.
6. To display the data stored in database this project fetches the details from database table "IMDBTop250",
   Then with the help of Xlsxwriter module it dumps the details into an excel created in the project Directory "IMDB/src/test" named "IMDB_Movie_List.xlsx".
7. After the data gets finished duming into an Excel the program automatically invokes the "IMDB_Movie_List.xlsx" Excel to display the all
   movie_names, release_year and the ratings with the help of "Subprocess" module.

