from dataclasses import dataclass
from abprocess.authenticator import Authenticator
from abprocess.booking_course import BookingCourse
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
