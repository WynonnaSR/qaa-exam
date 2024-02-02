from time import sleep
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from locators.strategies_and_locators import Strategies, PageLocators
from src.scripts import JsonScripts


class DedicatedServers:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_product_cards_by_filter(self, currency, min_price_value, max_price_value, label):
        driver = self.driver

        self.wait.until(
            ec.visibility_of_element_located((Strategies.XPATH, PageLocators.DEDICATED_SERVERS_BUTTON))).click()
        self.wait.until(
            ec.visibility_of_element_located((Strategies.XPATH, PageLocators.CURRENCY_SWITCH[currency]))).click()
        field_for_filter_min = self.wait.until(
            ec.visibility_of_element_located((Strategies.XPATH, PageLocators.INPUT_FIELD_MIN)))
        field_for_filter_max = self.wait.until(
            ec.visibility_of_element_located((Strategies.XPATH, PageLocators.INPUT_FIELD_MAX)))
        sleep(1)
        field_for_filter_min.clear()
        field_for_filter_max.clear()
        sleep(1)
        field_for_filter_min.send_keys(min_price_value)
        field_for_filter_max.send_keys(max_price_value)
        sleep(1)
        self.wait.until(ec.visibility_of_element_located((Strategies.XPATH, PageLocators.SHOW_MORE_BUTTON))).click()
        show_fewer_button = self.wait.until(
            ec.visibility_of_element_located((Strategies.XPATH, PageLocators.SHOW_FEWER_BUTTON)))

        driver.execute_script(JsonScripts.SCROLL_INTO_VIEW, show_fewer_button)

        price_cards = driver.find_elements(Strategies.XPATH, PageLocators.SERVER_CARD)

        cards_data = {}

        for card in price_cards:
            location = card.find_element(Strategies.XPATH, PageLocators.SERVER_LOCATION).text
            currency_label = card.find_element(Strategies.XPATH, PageLocators.PRICE_CURRENCY_LABEL).text
            price = card.find_element(Strategies.XPATH, PageLocators.SERVER_COST).text
            model_of_cpu = card.find_element(Strategies.XPATH, PageLocators.MODEL_OF_CPU).text
            ram_capacity = card.find_element(Strategies.XPATH, PageLocators.RAM_CAPACITY).text
            gpu = card.find_element(Strategies.XPATH, PageLocators.MODEL_OF_GPU).text
            storage_capacity = card.find_element(Strategies.XPATH, PageLocators.STORAGE_CAPACITY).text
            raid_type = card.find_element(Strategies.XPATH, PageLocators.RAID_TYPE).text
            bandwidth = card.find_element(Strategies.XPATH, PageLocators.BANDWIDTH).text
            included_traffic = card.find_element(Strategies.XPATH, PageLocators.INCLUDED_TRAFFIC).text

            key = (f'{location} {model_of_cpu} {ram_capacity} {gpu} {storage_capacity} {raid_type} {bandwidth} '
                   f'{included_traffic}')

            cards_data[key] = currency_label, price

        price_violations = []
        label_violations = []

        for title, price in cards_data.items():
            if not float(min_price_value) <= float(price[1]) <= float(max_price_value):
                price_violation_message = f"The price of the product {title} does not meet the conditions"
                price_violations.append(price_violation_message)

        for title, label_of_currency in cards_data.items():
            if label_of_currency[0] != label:
                label_violation_message = f"The currency of the product {title} does not meet the conditions"
                label_violations.append(label_violation_message)

        field_for_filter_min.clear()
        field_for_filter_max.clear()

        return price_violations, label_violations
