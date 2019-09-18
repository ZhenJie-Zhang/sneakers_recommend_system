from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")
driver.get("https://www.remove.bg/")

# cookies_dict = [{'domain': 'remove.bg',
#                 'expiry': 1568181581,
#                 'httpOnly': False,
#                 'name': '_gat',
#                 'path': '/',
#                 'secure': False,
#                 'value': '1'}, \
#                {'domain': 'remove.bg',
#                 'expiry': 1631253521,
#                 'httpOnly': False,
#                 'name': '_ga',
#                 'path': '/',
#                 'secure': False,
#                 'value': 'GA1.2.2031480261.1568181521'}, \
#                {'domain': 'www.remove.bg',
#                 'expiry': 1575957521,
#                 'httpOnly': False,
#                 'name': 'paddlejs_checkout_variant',
#                 'path': '/', 'secure': False, 'value': '{"inTest":true,"controlGroup":false,"isForced":false,"variant":"multipage-radio-payment-selected"}'}, {'domain': 'remove.bg', 'expiry': 1568267921, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.932197069.1568181521'}, {'domain': 'www.remove.bg', 'httpOnly': True, 'name': '_remove_bg_session', 'path': '/', 'secure': False, 'value': 'QJ2ZDRGMbaZbiZTwhAy6GtIpNRpgR7mTZdPduF7hGtCCPSXEEn4Uoc%2BQO3afjfg6CIDcqoAKPdaM3x8c9ObtnQUH8xrbEihUDZhvgAlE1baYhscPZCmlyQMas%2FDiW8AbRuwUhVkzzR1WB%2F400jXKXUu7iRJN9MuezMe4lApRNHVZ4ffOHN2BSfTQtaivKcOiVtcAJ%2BwB%2Bn7ZAMbwSOecnXbuCC1W7Hg25g%3D%3D--y%2Bm%2BIMRXRbFj1hsp--gO4dxAeHoC%2FIkW8JqSUURg%3D%3D'}, {'domain': 'remove.bg', 'expiry': 1599717522, 'httpOnly': False, 'name': '_hjid', 'path': '/', 'secure': False, 'value': 'e24aad54-9f07-4779-b831-24fca91dec7b'}, {'domain': 'remove.bg', 'expiry': 1599717520.084556, 'httpOnly': True, 'name': '__cfduid', 'path': '/', 'secure': True, 'value': 'd53754b03e0dd7110a81a7276687c19191568181519'}

cookies = [{'domain': '.google.com', 'name': '1P_JAR', 'value': '2019-9-11-5'},
           {'domain': '.google.com', 'name': 'ANID', 'value': 'AHWqTUmLETA0mVNvTWDA3hRZE80GUciBxfYMpNCZy-5sZQwL4_ZRKyCQqSsBz6Kt'},
           {'domain': '.google.com', 'name': 'APISID', 'value': '2c7gk1a1oAy2RPVQ/Av8RKIHavaS-VRRAC'},
           {'domain': '.google.com', 'name': 'HSID', 'value': 'AFsldYsbMIKsyplM3'},
           {'domain': '.google.com', 'name': 'NID', 'value': '188=MnahF7qQ1vEM0K32_URSxT9CGlSxgJs5N7-KFkrQbYnAXKM9DgTh5iTRKfbiSIEEsN8UJ7eV7QZ-cKCm9RWBm5thR-P2BMtAnluME55_h8-fYWewv3jX8x5R466jrVQJPYlNTR1Qi8XPThbk9UQPcCIq1M3ndH47j4EFiiv2msCt6ZKnijEBZxlN3-UZ6wLqoQssggb8Ksn0WLJwWBja7i7Ugq9Azc2ADdqmphW9wYHW3VOQ2kSie3fdESugnHb7G-j2nvWAWb2iF4-fWMBLw7V4XXrUD-FslgaCre6WXL9S'},
           {'domain': '.google.com', 'name': 'SAPISID', 'value': '1c2vLMx7QGa03nBM/Ah50mE4mJhRy_Pvgk'},
           {'domain': '.google.com', 'name': 'SID', 'value': 'nweX_Z9KNc8MdqtNZGbdDMeSdgMLZRBAzQl9hXLPq5xtMOuPZwAxGnyANeAH_sstdVZvxQ.'},
           {'domain': '.google.com', 'name': 'SIDCC', 'value': 'AN0-TYtkuKhFdUk3bSOt1qiSCB2EPk9G2KrhuHF-4__YixaswAGK9Q2DHqDyCdCA0NCvqTcJSQ'},
           {'domain': '.google.com', 'name': 'SSID', 'value': 'AmV_eoyqLpX7UTw58'},
           {'domain': 'www.google.com', 'name': 'OTZ', 'value': '5069247_24_24__24_'},
           {'domain': '.gstatic.com', 'name': '1P_JAR', 'value': '2019-09-09-03'}]

for cookie in cookies:
    driver.add_cookie(cookie)

# driver.add_cookie({'domain': '.google.com', 'name': '1P_JAR', 'value': '2019-9-11-5'})

print(driver.get_cookies())
sleep(3)
driver.find_element_by_xpath('//*[@id="colorlib-logo"]/a').click()
print(driver.get_cookies())
sleep(10)
