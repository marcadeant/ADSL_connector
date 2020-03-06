from dataclasses import dataclass
import json
import sys
import logging
from time import sleep
from selenium import webdriver
from abprocess.constants import USER_NAME_XPATH, PASSWORD_XPATH, CONFIRM_BUTTON_XPATH, TIME_SLEEP
import os
logger = logging.getLogger()

@dataclass
class Authenticator:

    browser: webdriver
    host_url: str = 'https://www.adsltennis.fr/_start/index.php?club=57920017'

    def adsl_connector(self):

        with open(os.getcwd() + '/auth.json', 'r') as json_file:
            token = json.load(json_file)

        logger.info(f'Searching for this url :{self.host_url}')

        self.browser.get(self.host_url)

        try:
            logger.info('connexion to ADSL portail..')
            input_user_name = self.browser.find_element_by_xpath(USER_NAME_XPATH)
            input_user_name.send_keys(token['user_name'])
            logger.info('User name verified')
            sleep(TIME_SLEEP)
            input_pwd = self.browser.find_element_by_xpath(PASSWORD_XPATH)
            input_pwd.send_keys(token['password'])
            logger.info('password verified')
            sleep(TIME_SLEEP)
            submit = self.browser.find_element_by_xpath(CONFIRM_BUTTON_XPATH)
            submit.click()
            logger.info('connexion succeeded')
            sleep(TIME_SLEEP)
        except Exception:
            logger.error(f'connexion to ADSL portail failed. Please check your internet access and retry the process')
            self.browser.quit()
            sys.exit()






