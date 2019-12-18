from pageobjects.core.elements import Element
from pageobjects.locators import travel_insurance_page_locators as locators


class DatePickerElement(Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def select_date_by_day(self, day):
        day_locator = locators.DATE_PICKERS['DATE_OPTION']
        day_locator = (day_locator[0], day_locator[1].format(day=day))
        self.select_date_by_day_locator(day_locator)

    def select_date_by_day_locator(self, day_locator):
        self.click()
        day_element = Element(day_locator, self._driver)
        day_element.click(move_to_element=True)
