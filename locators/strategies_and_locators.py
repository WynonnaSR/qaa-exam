class Strategies:
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"


class PageLocators:
    DEDICATED_SERVERS_BUTTON = '//div[@class="gc-server-configurator-buttons"]/button[1]'
    VIRTUAL_SERVERS_BUTTON = '//div[@class="gc-server-configurator-buttons"]/button[2]'
    SHOW_MORE_BUTTON = '//div[@class="gc-text_16 gc-server-configurator-more"]'
    SHOW_FEWER_BUTTON = '//div[@class="gc-flex gc-flex-h-center gc-m-top_xx-large gc-server-configurator__fixed-block"]'

    CURRENCY_SWITCH = {
        'eur': '//div[@class="gc-switcher gc-switcher_orange-gray"]/label[1]',
        'usd': '//div[@class="gc-switcher gc-switcher_orange-gray"]/label[2]'
    }
    # EUR_CURRENCY_SWITCH = '//div[@class="gc-switcher gc-switcher_orange-gray"]/label[1]'
    # USD_CURRENCY_SWITCH = '//div[@class="gc-switcher gc-switcher_orange-gray"]/label[2]'

    INPUT_FIELD_MIN = '//div[@class="gc-configurator-filter-table-inputs"]/gcore-input-field[1]/div/input'
    INPUT_FIELD_MAX = '//div[@class="gc-configurator-filter-table-inputs"]/gcore-input-field[2]/div/input'

    SERVER_CARD = '//div[@class="price-card"]'
    SERVER_NAME_LABEL = './/p[@class="gc-text gc-text_16 gc-text_regular gc-text-color_primary gc-m-bottom_medium"]'
    PRICE_CURRENCY_LABEL = './/div[@class="price-card_price"]/sub[1]'
    SERVER_COST = './/div[@class="price-card_price"]/span'

    # Locators for dedicated server parameters
    SERVER_LOCATION = './/p[@class="gc-text gc-text-color_primary gc-text_20 gc-text_medium gc-m-top_x-large"]'
    MODEL_OF_CPU = './/ul[@class="gc-m-top_x-large price-card_params"]/li[1]/div[2]'
    RAM_CAPACITY = './/ul[@class="gc-m-top_x-large price-card_params"]/li[2]/div[2]'
    MODEL_OF_GPU = './/ul[@class="gc-m-top_x-large price-card_params"]/li[3]/div[2]'
    STORAGE_CAPACITY = './/ul[@class="gc-m-top_x-large price-card_params"]/li[4]/div[2]'
    RAID_TYPE = './/ul[@class="gc-m-top_x-large price-card_params"]/li[5]/div[2]'
    BANDWIDTH = './/ul[@class="gc-m-top_x-large price-card_params"]/li[6]/div[2]'
    INCLUDED_TRAFFIC = './/ul[@class="gc-m-top_x-large price-card_params"]/li[7]/div[2]'
