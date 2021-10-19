from selenium.webdriver.common.by import By
from selenium import webdriver


class TestMantis():
  def setup_method(self, method):
    self.driver = webdriver.Chrome('drivers/chrome94/chromedriver.exe')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_mantis(self):
    self.driver.get('https://iterasys.com.br/plataforma/home/index.php?action=initial')
    self.driver.set_window_size(1696, 1066)
    self.driver.find_element(By.ID, "searchtext").click()
    self.driver.find_element(By.ID, "searchtext").send_keys("mantis")
    self.driver.find_element(By.CSS_SELECTOR, ".fa-search").click()
    self.driver.find_element(By.CSS_SELECTOR, ".comprar").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".item-title").text == "Mantis"
    assert self.driver.find_element(By.CSS_SELECTOR, ".subtotal").text == "SUBTOTAL R$ 59,99"
  
