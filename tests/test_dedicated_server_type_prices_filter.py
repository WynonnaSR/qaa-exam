import allure
import pytest
from allure import title
from selenium import webdriver
from operations.dedicated_servers import DedicatedServers


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('window-size=1368x768')
options.set_capability('browserName', 'chrome')
options.set_capability('browserVersion', '120.0')
# If there are issues with .set_capability(), you can try using .add_experimental_option()
# options.add_experimental_option('browserName', 'chrome')
# options.add_experimental_option('version','120.0')
driver = webdriver.Chrome(options=options)
url = 'https://gcore.com/hosting'


@pytest.mark.parametrize('currency, min_price_value, max_price_value', [
    ('eur', '89', '274'),
    ('usd', '93', '373')
])
def test_usd_currency_cards(currency, min_price_value, max_price_value):
    driver.get(url)
    labels = {'usd': '$', 'eur': '€'}
    label = labels[currency]

    hosting_page = DedicatedServers(driver)
    price_violations, label_violations = hosting_page.get_product_cards_by_filter(currency, min_price_value, max_price_value, label)
    with allure.step("check price"):
        if price_violations:
            raise AssertionError("\n".join(price_violations))

    with allure.step("check currency label"):
        if label_violations:
            raise AssertionError("\n".join(label_violations))

    driver.quit()


