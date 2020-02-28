from dataclasses import dataclass
from datetime import datetime
from time import sleep
from abprocess.authenticator import Authenticator

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from abprocess.constants import TENNIS_COURT_NAME, PICK_PLAYER_MENU_ID, PLAYER_NAME_XPATH, \
    BOOKING_CONFIRMATION_BUTTON_XPATH, NEXT_DAY_BUTTON_XPATH, TIME_SLEEP
import logging
import sys

logger = logging.getLogger()


@dataclass
class BookingCourse:
    tennis_course_name: str
    tennis_course_hour: int  # format 24h
    tennis_course_date: str  # format dd-mm-yyyy
    player_name: str
    authenticator: Authenticator
    times_count: int = 0
    booking: bool = False

    def __post_init__(self):
        self.tennis_course_day_datetime = datetime.strptime(self.tennis_course_date, '%d/%m/%Y')
        self.browser = self.authenticator.browser

    def __repr__(self):
        return f"date: {self.tennis_course_date}, tennis court :{self.tennis_course_name}, hour: {self.tennis_course_hour}"

    # get the number of click to do on the next_day_button
    def next_day_button_number(self):

        today = datetime.now()
        time_delta = self.tennis_course_day_datetime - today
        next_day_number = time_delta.days

        return next_day_number

    def booking_course(self, browser: webdriver.Chrome, tennis_court_name: str):

        decode_course_name = TENNIS_COURT_NAME[tennis_court_name]

        if self.times_count == 0:
            next_day_button = browser.find_element_by_xpath(NEXT_DAY_BUTTON_XPATH)
            number_of_click = self.next_day_button_number()
            for i in range(number_of_click + 1):
                next_day_button.click()
                sleep(TIME_SLEEP)
            self.times_count = + 1
        # Catch error if date isn't available

        try:
            logger.info(f'Trying to reserve : {tennis_court_name}')
            double_click_action = ActionChains(browser)
            web_element_id = str(self.tennis_course_hour) + '_0_' + decode_course_name
            booking_course = browser.find_element_by_id(web_element_id)
            double_click_action.double_click(booking_course).perform()
            sleep(5)
            if tennis_court_name == 'A':
                mojjo_accept_button = browser.find_element_by_xpath('/html/body/div[7]/button[1]')
                mojjo_accept_button.click()
                sleep(TIME_SLEEP)
            player_name_menu = browser.find_element_by_id(PICK_PLAYER_MENU_ID)
            logger.info('Picking players menu...')
            player_name_menu.click()
            sleep(TIME_SLEEP)
            logger.info(f'Finding player name : {self.player_name}')
            pick_player = browser.find_element_by_xpath(PLAYER_NAME_XPATH[self.player_name])
            pick_player.click()
            sleep(TIME_SLEEP)
            logger.info(f'The sessions {self.__repr__()} has been successfully reserved')
            booking_confirmation = browser.find_element_by_xpath(BOOKING_CONFIRMATION_BUTTON_XPATH)
            booking_confirmation.click()
            sleep(TIME_SLEEP)
            browser.quit()
            self.booking = True
        except Exception:
            logger.error(f'The session {self.__repr__()} already reserved, {tennis_court_name}')

    def booking_courses_by_priorities(self, browser: webdriver.Chrome):


        for tennis_court_name in TENNIS_COURT_NAME.keys():

            if not self.booking:
                self.booking_course(browser, tennis_court_name)

        if not self.booking:
            logger.error('No tennis court available for this session')
