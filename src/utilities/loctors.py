from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name


class IMDBHomePageLocators(object):
  LOGO                   = (By.ID, 'home_img')
  TITLE                  = "IMDb Top 250 - IMDb"
  CHART_TABLE_SIZE       = (By.XPATH, ".//table[@data-caller-name='chart-top250movie']//tr")
  LINKS                  = ".//table[@class='chart full-width']//tr//td[@class='titleColumn']/a"
  MOVIE_NAME_COLUMN      = ".//table[@class='chart full-width']//tr[0]//td[@class='titleColumn']/a"
  MOVIE_YEAR_COLUMN      = ".//table[@class='chart full-width']//tr[0]//td[@class='titleColumn']/span"
  MOVIE_RATING_COLUMN    = ".//table[@class='chart full-width']//tr[0]//td[@class='ratingColumn imdbRating']/strong"
