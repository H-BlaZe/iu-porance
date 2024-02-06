# from flask import Blueprint, render_template, request
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
#
# views = Blueprint(__name__, "views")
#
#
# @views.route("/")
# def home():
#     return render_template("index.html")
#
#
# @views.route("/attendance-data", methods=["POST"])
# def submitForm():
#     enr_no = request.form.get("enr")
#     pwd_no = request.form.get("pwd")
#
#     driver_service = webdriver.Chrome("C:\\Users\\Webdriver\\chromedriver.exe")
#
#     url = "https://sms.iul.ac.in/Student/login.aspx"
#     data = {"txtun": enr_no, "txtpass": pwd_no, "btnlog": "LOGIN"}
#
#     response = requests.post(url, data=data)
#     print(response.content)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     usrname_textbox = soup.find('span', id= 'lblUname')
#     name = usrname_textbox.get_text(strip=True)
#     print('Value of the textbox:', name)
#     return render_template("data.html", name=name)
#
#


from flask import Flask, render_template, request, Blueprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route('/attendance-data', methods=['POST'])
def submit_form():
    enr_no = request.form.get("enr")
    pwd_no = request.form.get("pwd")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver_service = Service(executable_path="C:\\Users\\Webdriver\\chromedriver.exe")
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    try:
        # Navigate to the login page
        driver.get('https://sms.iul.ac.in/Student/login.aspx')

        # Fill out the enrollment number and password fields
        driver.find_element(By.ID, "txtun").send_keys(enr_no)
        driver.find_element(By.ID, "txtpass").send_keys(pwd_no)

        # Click the login button
        driver.find_element(By.ID, "btnlog").click()

        name = driver.find_element(By.ID, "lblUname")

        return render_template('data.html', name=name.text)

    except Exception as e:
        return f'Error: {e}'



