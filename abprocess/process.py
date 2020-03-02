from dataclasses import dataclass

from abprocess.authenticator import Authenticator
from abprocess.booking_course import BookingCourse
from abprocess.logger import LogFileHandler
import logging
import json
from selenium import webdriver
from datetime import datetime
from time import sleep
from abprocess.constants import TIME_SLEEP


@dataclass
class Process:
    authenticator: Authenticator
    booking_course: BookingCourse

    def process(self):

        self.authenticator.adsl_connector()
        # Keeping the same session opened by authenticator class
        browser = self.authenticator.browser
        sleep(TIME_SLEEP)
        self.booking_course.booking_courses_by_priorities(browser)



def main():

    logger = logging.getLogger()
    LogFileHandler(logger=logger).set_log_configuration()

    logger.info('From main : Starting Process')

    logger.info('Reading parameters...')
    with open('../parameters.json', 'r') as json_file:
        parameters = json.load(json_file)
    logger.info(f"Starting process for date : {parameters['date']}, hour : {parameters['hour']}, player : {parameters['player_name']} ")
    start = datetime.now()
    logger.info('Launching Chrome application')
    # Starting a new browser session
    browser = webdriver.Chrome('/Users/amarcade/Documents/ADSL_connector/abprocess/chromedriver')
    authenticator = Authenticator(browser=browser)
    booking_course = BookingCourse(tennis_course_date=parameters['date'], tennis_course_hour=parameters['hour'], tennis_course_name='A',
                                   player_name=parameters['player_name'])
    process = Process(authenticator=authenticator, booking_course=booking_course)
    process.process()
    end = datetime.now()
    time = end - start
    logger.info(f"process finished in {time.seconds} seconds")


if __name__ == '__main__':
    main()
