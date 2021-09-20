# import webapi

# webapi.create_session()

# webapi.get("https://www.facebook.com")

# webapi.screenshot("1st")



from webapi import WebAPI

driver = WebAPI()
driver.get("https://www.google.com")
driver.screenshot('xyz')