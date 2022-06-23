"""
This main.py is a python selenium testing script for guide.html.
The solutions are provided in methods called test1, test2, test3... test6

NOTE:
1. I chose python selenium library for my tests
2. For the guide_page, I used local html page so guide_page path NEEDS TO BE CHANGED in other machine.
3. I used different chrome drive PATH so this also NEEDS TO BE CHANGED in other machine.
"""

import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"D:\Programming projects\Python project files\Resolver test"
guide_page = "file:///D:/Programming%20projects/Python%20project%20files/Resolver%20test/guide.html"
driver = webdriver.Chrome()


# --------------- Methods  --------------------

def navigate_homepage(driver, starting_page=guide_page):
    """
    Connects to the guide page and then navigates to homepage.
    :param driver: connection to the Chrome browser
    :param starting_page: guide_page.html (local)
    :return: void
    """
    driver.get(guide_page)
    driver.implicitly_wait(60)

    # navigating to homepage
    element = driver.find_element(By.CLASS_NAME, 'nav-link')
    home_page = element.get_attribute('href')
    driver.get(home_page)


def test1(driver):
    """
    1. Navigate to home page
    2. Assert that both the email address and password inputs are present as well as the login button
    3. Enter in an email address and password combination into the respective fields
    :param driver: connection to Chrome browser
    :return: void
    """
    # navigating to home page
    navigate_homepage(driver, guide_page)

    # Get the email, password and login button from the homepage
    email = driver.find_element(By.ID, 'inputEmail')
    password = driver.find_element(By.ID, 'inputPassword')
    log_in_button = driver.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-block')

    # this try should fail because email and password are currently empty
    try:
        assert email.text != ""
        assert password.text != ""
        assert log_in_button is not None

        raise Exception("The assert statements failed to find the problem")
    except AssertionError:
        print("Test 1: The assert statements work")

    # Now that the assert statements work, we fill in the email and password
    email.send_keys("testing_email@gmail.com")
    password.send_keys("password_protected")


def test2(driver):
    """
    1. Navigate to home page
    2. In the test 2 div, assert that there are three values in the listgroup
    3. Assert that the second list item's value is set to "List Item 2"
    4. Assert that the second list item's badge value is 6
    :param driver: connection to Chrome browser
    :return: void
    """
    # navigating to home page
    navigate_homepage(driver, guide_page)

    # Finding the number of elements inside the list
    count = 0
    item_list = []

    list = driver.find_element(By.CLASS_NAME, 'list-group')
    items = list.find_elements(By.TAG_NAME, 'li')
    for item in items:
        count += 1
        item_list.append(item.text)
    assert count == 3  # Is there exactly 3 elements in the list?

    # Getting the value for second item
    second_item = item_list[1]
    assert "List Item 2" in str(second_item)  # Does the second element called List Item 2?

    # Getting the badges for all the items
    badge_list = []
    badges = driver.find_elements(By.CLASS_NAME, 'badge.badge-pill.badge-primary')
    for badge in badges:
        badge_list.append(badge.text)
    second_badge = badge_list[1]
    assert 6 == int(second_badge)  # Is the badge for second element == 6?


def test3(driver):
    """
    1. Navigate to the home page
    2. In the test 3 div, assert that "Option 1" is the default selected value
    3. Select "Option 3" from the select list
    :param driver: connecting to Chrome browser
    :return: void
    """
    # navigating to home page
    navigate_homepage(driver, guide_page)

    # After loading the home page, I want to get the first selected option
    # from the drop down list because that is the default option
    drop_down = driver.find_element(By.CLASS_NAME, 'dropdown')
    button_drop_down = driver.find_element(By.CLASS_NAME, 'btn.btn-secondary.dropdown-toggle')
    expanded = button_drop_down.get_attribute('aria-expanded')

    # Assert statements proves (The drop down list is untouched, not expanded and its on Option 1)
    assert expanded == 'false'
    assert drop_down.text == 'Option 1'

    # Now we need to select Option 3 in the drop down button.
    button_drop_down.click()
    WebDriverWait(driver, 3)
    button = driver.find_element(By.LINK_TEXT, 'Option 3')
    button.click()


def test4(driver):
    """
    1. Navigate to home page
    2. In the test 4 div, assert that the first button is enabled and that the second button is disabled
    :param driver: connecting to Chrome browser
    :return: void
    """
    # navigating to home page
    navigate_homepage(driver, guide_page)

    first_button = driver.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary')
    assert first_button.is_enabled()

    second_button = driver.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-secondary')
    assert second_button.is_enabled() is False


def test5(driver):
    """
    1. Navigate to home page
    2. In the test 5 div, wait for a button to be displayed (note: the delay is random) and then click it
    3. Once you've clicked the button, assert that a success message is displayed
    4. Assert that the button is now disabled
    :param driver: connecting to Chrome browser
    :return: void
    """
    # navigating to home page
    navigate_homepage(driver, guide_page)

    # Need to wait for the button before clicking it
    WebDriverWait(driver, 60).until(

        EC.element_to_be_clickable((By.XPATH, '//*[@id="test5-button"]'))
    )
    button = driver.find_element(By.XPATH, '//*[@id="test5-button"]')
    button.click()


def test6(driver):
    """
    1. Navigate to home page
    2. Write a method that allows you to find the value of any cell on the grid
    3. Use the method to find the value of the cell at coordinates 2, 2 (staring at 0 in the top left corner)
    4. Assert that the value of the cell is "Ventosanzap"
    :param driver: connecting to Chrome driver
    :return: void
    """
    # navigating to home page
    navigate_homepage(driver, guide_page)

    value = find_table_val(2, 2)
    assert value == 'Ventosanzap'


def find_table_val(row_num, col_num):
    """
    Connects to home_page, test 6 table and finds out the grid value according to the coordinates in param.
    :param row_num: the row number of the grid (0-2)
    :param col_num: the col number of the grid (0-2)
    :return: if successful:
                grid's text value
             else: None
    """
    table = driver.find_element(By.CLASS_NAME, 'table.table-bordered.table-dark')
    rows = table.find_elements(By.TAG_NAME, 'tr')

    if row_num < 0 or row_num > 2 or col_num < 0 or col_num > 2:
        print("row_num and col_num values must be between 0 and 2")
        return None
    row_num = row_num + 1  # in my case, row 0 is the heading row

    try:
        col = rows[row_num].find_elements(By.TAG_NAME, 'td')[col_num]
        return str(col.text)
    except:
        return None

# --------------- Methods ends here --------------------


# --------------- Method calls --------------------

# test1(driver)
# test2(driver)
# test3(driver)
# test4(driver)
# test5(driver)
# test6(driver)
