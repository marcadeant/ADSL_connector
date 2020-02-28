import logging

from selenium import webdriver

from abprocess.authenticator import Authenticator
from abprocess.booking_course import BookingCourse
from datetime import datetime

from abprocess.logger import LogFileHandler
from abprocess.process import Process

logger = logging.getLogger()
LogFileHandler(logger=logger).set_log_configuration()

logger.info('From main : Starting Process')

start = datetime.now()
logger.info('Launching Chrome application')
browser = webdriver.Chrome('/Users/amarcade/Documents/ADSL_connector/abprocess/chromedriver')
authenticator = Authenticator(browser=browser)
booking_course = BookingCourse(tennis_course_date='29/02/2020', tennis_course_hour=13, tennis_course_name='A',
                               player_name='Simon', authenticator=authenticator)
process = Process(authenticator=authenticator, booking_course=booking_course, browser=browser)
process.process()
end = datetime.now()
time = end - start
print(f"process finished in {time.seconds} seconds")
