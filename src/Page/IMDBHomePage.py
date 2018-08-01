from main.PageObject import Page
from utilities.loctors import IMDBHomePageLocators
from selenium.webdriver.common.by import By
from utilities.database import IMDBDatabase
import requests
import subprocess
import xlsxwriter

# Tests in form of Methods, each and every action on UI is being performed through this Page class


class IMDBHomePage(Page):

    def check_page_loaded(self):
        return True if self.find_element(*IMDBHomePageLocators.LOGO).is_displayed() else False

    def verify_title_matches(self):
        print(self.get_title())
        print(IMDBHomePageLocators.TITLE)
        return True if self.get_title() == IMDBHomePageLocators.TITLE else False

    def verify_broken_links(self):
        broken_link_text = []
        for link in range(len(self.find_elements(By.XPATH, IMDBHomePageLocators.LINKS))):
            r = requests.head(self.find_elements(By.XPATH, IMDBHomePageLocators.LINKS)[link].get_attribute("href"), verify= False, headers={"content-type":"text"})
            if r.status_code > 400:
                broken_link_text.append(self.find_elements(By.XPATH, IMDBHomePageLocators.LINKS)[link].text)
                print("Invalid/Broken Link")
        return broken_link_text

    def fetch_data(self):
        movie_name = []
        movie_year = []
        movie_rating = []
        for i in range(1, len(self.find_elements(*IMDBHomePageLocators.CHART_TABLE_SIZE))):
            IMDBHomePageLocators.MOVIE_NAME_COLUMN = IMDBHomePageLocators.MOVIE_NAME_COLUMN.replace(str(i-1), str(i))
            movie_name.append(self.find_element(By.XPATH, IMDBHomePageLocators.MOVIE_NAME_COLUMN).text)

            IMDBHomePageLocators.MOVIE_YEAR_COLUMN = IMDBHomePageLocators.MOVIE_YEAR_COLUMN.replace(str(i-1), str(i))
            movie_year.append(self.find_element(By.XPATH, IMDBHomePageLocators.MOVIE_YEAR_COLUMN).text)

            IMDBHomePageLocators.MOVIE_RATING_COLUMN = IMDBHomePageLocators.MOVIE_RATING_COLUMN.replace(str(i - 1), str(i))
            movie_rating.append(self.find_element(By.XPATH, IMDBHomePageLocators.MOVIE_RATING_COLUMN).text)
        return {"Movie_Name": movie_name, "Movie_Year": movie_year, "Movie_Rating": movie_rating}

    def insert_into_db(self, data):
        conn = IMDBDatabase.connect()
        c = conn.cursor()
        data_list = list(data.keys())
        print("create table IMDBTop250 ("+data_list[0]+" text"+data_list[1]+" text"+data_list[2]+" text"")")
        query = "create table IMDBTop250 ("+data_list[0]+" text,"+data_list[1]+" text,"+data_list[2]+" text"")"
        IMDBDatabase.exec_query(c, query)

        mapped = zip(data['Movie_Name'], data['Movie_Year'], data['Movie_Rating'])
        list_mapped = list(mapped)
        query = "INSERT into IMDBTop250 values(?,?,?)"
        for i in range(len(data['Movie_Name'])-1):
            IMDBDatabase.exec_insert_query(c, query, list_mapped[i])
            # print(list_mapped[i])
        return c.execute("Select * from IMDBTop250")

    def display_db_data(self, data):
        a = list(zip(data))
        print(a)
        print(len(a))
        workbook = xlsxwriter.Workbook("IMDB_Movie_List.xlsx")
        worksheet = workbook.add_worksheet()
        col = 0
        worksheet.set_column(1, 1, 15)

        # Write some data headers.
        worksheet.write('A1', 'Movie_Name')
        worksheet.write('B1', 'Movie_Year')
        worksheet.write('C1', 'Movie_Rating')
        row = 1
        col = 0

        for i in range(len(a)):
            counter = 0
            worksheet.write_string(row, col, a[i][0][counter])
            worksheet.write_string(row, col+1, a[i][0][counter+1])
            worksheet.write_string(row, col+2, a[i][0][counter+2])
            row += 1

        workbook.close()
        subprocess.Popen(["IMDB_Movie_List.xlsx"], shell=True)



