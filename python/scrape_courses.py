from selenium import webdriver
import time
import re
import json # Use is json.dumps(object)

valid_semesters = ['S', 'F', 'W', 'SUM']
valid_frequency = ['IRR', 'Y', 'E']


def scrape_department_links(url):
    browser = webdriver.Chrome()
    browser.get(url)

    department_links = []
    atoz_div = browser.find_element_by_id('atozindex')
    atoz_links = atoz_div.find_elements_by_tag_name('a')
    for link in atoz_links:
        href = link.get_attribute('href')
        if href is not None:
            department_links.append(href)
    browser.close()
    return department_links


def scrape_courses(url, courses):
    browser = webdriver.Chrome()
    browser.get(url)
    dept_courses = browser.find_elements_by_class_name('courseblock')
    for course in dept_courses:
        course_json = dict()
        course_title_block = course.find_element_by_class_name('courseblocktitle').text
        course_title_block_array = course_title_block.split()
        course_dept = course_title_block_array[0]
        course_number = course_title_block_array[1]
        course_name = ' '.join(course_title_block_array[2:-1])
        course_desc_block = course.find_element_by_class_name('courseblockdesc').text
        course_credits = course_desc_block.split()[-2]  # TODO: SHOULD 1-3 Credits be broken into 3 different courses with the same info, or can it be a range
        course_semesters_and_frequency = course_desc_block[course_desc_block.rfind('(')+1:course_desc_block.rfind(')')]\
            .replace('-', ' ').replace(',', ' ').split()
        course_semesters = []
        course_frequency = ''
        for data in course_semesters_and_frequency:
            if data in valid_semesters:
                course_semesters.append(data)
            elif data in valid_frequency:
                course_frequency = data
        course_prereqs = []
        course_prereqs_dirty =

        # Put Data into the Dictionary
        course_json['department'] = course_dept # Department

    browser.close()


def main():
    department_links = scrape_department_links('https://catalog.ithaca.edu/undergrad/coursesaz/')
    courses = []
    for department_link in department_links:
        scrape_courses(department_link, courses)
        time.sleep(2)


main()
