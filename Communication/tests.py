# python manage.py test communication
# Ran 1 test in 4.432s
#OK

from django.test import TestCase
# Code I wrote

from channels.testing import ChannelsLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

# Create your tests here.
class ChatConsumerTests(ChannelsLiveServerTestCase):
    serve_static = True  # Emulate the live server static file serving

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_can_connect_to_chat_and_send_messages(self):
        try:
            self.driver.get(self.live_server_url + "/chat/general/")
            self.assertIn("My Learning Site", self.driver.title)

            # Simulate a user entering a message
            message_input = self.driver.find_element(By.ID, "chat-message-input")
            message_input.send_keys("Hello, world!")

            # Simulate sending the message
            send_button = self.driver.find_element(By.ID, "chat-message-submit")
            send_button.click()

            # Wait for the message to be displayed
            WebDriverWait(self.driver, 2).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".chat-log"), "Hello, world!")
            )

        finally:
            time.sleep(3)  # Keep the browser open for 3 seconds

# End of Code I wrote