import logging

from selenium import webdriver
import json
from abprocess.authenticator import Authenticator
from abprocess.booking_course import BookingCourse
from datetime import datetime

from abprocess.logger import LogFileHandler
from abprocess.process import Process
import os

logger = logging.getLogger()
LogFileHandler(logger=logger).set_log_configuration()

logger.info('From main : Starting Process')

logger.info('Reading parameters...')
with open('parameters.json', 'r') as json_file:
    parameters = json.load(json_file)
logger.info(
    f"Starting process for date : {parameters['date']}, hour : {parameters['hour']}, player : {parameters['player_name']} ")
start = datetime.now()
logger.info('Launching Chrome application')
# Starting a new browser session
path = os.getcwd()
browser = webdriver.Chrome(path+'/abprocess/chromedriver')
authenticator = Authenticator(browser=browser)
booking_course = BookingCourse(tennis_course_date=parameters['date'], tennis_course_hour=parameters['hour'],
                               tennis_course_name='A',
                               player_name=parameters['player_name'])
process = Process(authenticator=authenticator, booking_course=booking_course)
process.process()
end = datetime.now()
time = end - start
logger.info(f"process finished in {time.seconds} seconds")

