from dataclasses import dataclass

from abprocess.authenticator import Authenticator
from abprocess.booking_course import BookingCourse
from abprocess.logger import LogFileHandler
import logging
from selenium import webdriver
from datetime import datetime
from time import sleep


@dataclass
class Process:
    authenticator: Authenticator
    booking_course: BookingCourse
    browser: webdriver

    def process(self):


        self.authenticator.adsl_connector()
        # browser is obtained after the authentications
        # requests maintained by the authenticator class
        browser = self.authenticator.browser
        sleep(10)
        self.booking_course.booking_courses_by_priorities(browser)



def main():

    logger = logging.getLogger()
    LogFileHandler(logger=logger).set_log_configuration()

    logger.info('From main : Starting Process')

    start = datetime.now()
    logger.info('Launching Chrome application')
    browser = webdriver.Chrome('/Users/amarcade/Documents/ADSL_connector/abprocess/chromedriver')
    authenticator = Authenticator(browser=browser)
    booking_course = BookingCourse(tennis_course_date='29/02/2020', tennis_course_hour=17, tennis_course_name='A',
                                   player_name='Simon', authenticator=authenticator)
    process = Process(authenticator=authenticator, booking_course=booking_course, browser=browser)
    process.process()
    end = datetime.now()
    time = end - start
    print(f"process finished in {time.seconds} seconds")


if __name__ == '__main__':
    main()
