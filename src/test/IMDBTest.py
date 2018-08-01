import unittest
from selenium import webdriver
from src.Page.IMDBHomePage import IMDBHomePage

# Test Class


class Test_GetTop250MovieDetails(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\IMDB\\Lib\\chromedriver.exe")
        self.driver.get("https://www.imdb.com/chart/top")

    def test_imdb_page(self):
        # print("\n" + str(test_cases(0)))
        page = IMDBHomePage(self.driver)
        self.assertTrue(page.check_page_loaded())
        self.assertTrue(page.verify_title_matches())
        broken_links = page.verify_broken_links()
        for link in broken_links:
            print(link.text)
        data_dict = page.fetch_data()
        print(data_dict['Movie_Name'])
        print(data_dict['Movie_Year'])
        print(data_dict['Movie_Rating'])
        data_row = page.insert_into_db(data_dict)
        print(data_row)
        page.display_db_data(data_row)

    def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_GetTop250MovieDetails)
    unittest.TextTestRunner(verbosity=2).run(suite)
