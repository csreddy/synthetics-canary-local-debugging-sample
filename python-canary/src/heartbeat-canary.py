"""
This is a sample heartbeat canary to run in local dev environment.
"""
from aws_synthetics.selenium import synthetics_webdriver as syn_webdriver
from aws_synthetics.common import synthetics_logger as logger
from faker import Faker
faker = Faker()

def main():      
    logger.info("UUID: " + faker.uuid4())
    url = "https://www.example.com/"
    browser = syn_webdriver.Chrome()
    browser.get(url)
    browser.save_screenshot("loaded.png")

    response_code = syn_webdriver.get_http_response(url)
    if not response_code or response_code < 200 or response_code > 299:
        raise Exception("Failed to load page!")
    
    logger.info("Canary successfully executed.")


def handler(event, context):
    return main()