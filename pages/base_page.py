from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание кликабельности элемента: {locator}")
    def wait_element_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидание загрузки элемента: {locator}")
    def wait_for_load_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))

    @allure.step("Клик по кнопке: {locator}")
    def click_button(self, locator):
        self.wait_element_clickable(locator)
        self.driver.find_element(*locator).click()

    @allure.step("Ввод текста в поле: {locator}, текст: {text}")
    def send_keys_to_field(self, locator, text):
        self.wait_element_clickable(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step("Получить текст элемента: {locator}")
    def get_text_locator(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    @allure.step("Получить список элементов: {locator}")
    def get_text_locators(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Проверка отображения элемента: {locator}")
    def check_element(self, locator):
        self.wait_for_load_element(locator)
        return self.driver.find_element(*locator)

    @allure.step("Проверка, что элемент не отображается: {locator}")
    def check_element_is_not_visible(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Перетаскивание элемента: {element_one} → {element_two}")
    def drag_and_drop(self, element_one, element_two):
        element = self.driver.find_element(*element_one)
        target = self.driver.find_element(*element_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    @allure.step("Наведение и клик по элементу: {locator}")
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()