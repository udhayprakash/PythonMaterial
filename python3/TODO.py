import os
import sys
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse, Message, Body

page = requests.get('https://www.worldometers.info/coronavirus/#countries')

soup = BeautifulSoup(page.content, 'html.parser')

table_body = soup.find('tbody')

table_body_all = soup.find

rows = table_body.find_all('tr')

application = Flask(__name__)



@application.route("/")
def home():
    return "App is Running..."

@application.route("/sms", methods=['GET','POST'])
def sms_replay():
    msg = request.values.get('Body')
    n1="\n"

    def search(list, msg):
        for i in range(len(list)):
            if list[i] == msg:
                return True
            else:


        

    for row in rows:
        cols=row.find_all('td')
    
        cols=[x.text.strip() for x in cols]


        if search(cols, msg):
            txtToSnd = (
                f"{cols[0].upper()}{n1}{n1}"
                f"Total Cases: {cols[1]}{n1}"
                f"Cases per 1 Million People: {cols[8]}{n1}"
                f"Recoverd: {cols[5]}{n1}"
                f"Deaths {cols[3]}{n1}{n1}"
                f"Reported First Case: {cols[10]}{n1}{n1}"
                f"About This Data: "
                f"{n1}{n1}"
                f"The coronavirus COVID-19 is affecting 203 countries and territories around the world and 2 international conveyances: the Diamond Princess cruise ship harbored in Yokohama, Japan, and the Holland America's MS Zaandam cruise ship. The day is reset after midnight GMT+0.{n1}{n1}"
                f"{n1}{n1}"
                f"To get worlwide data about coronavirus replay with <World>"
                f"{n1}{n1}"
                f"Sorce: https://www.worldometers.info/coronavirus/#countries"
                f"{n1}{n1}"
                f"Have Questions? Please Visit: https://www.who.int/news-room/q-a-detail/q-a-coronaviruses{n1}{n1}"
                f"Stay Home! Stay Safe!{n1}{n1}{n1}"
                f"DHAVAL VASVELIYA"
                )
            
            resp = MessagingResponse()
            resp.message(txtToSnd)

            return str(resp)
            
if __name__  == "__main__":
    application.run()