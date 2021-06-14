import requests
import datetime
import time
import schedule
import telegram
import os
from dotenv import load_dotenv

# For making the get request seem legit.
headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en;q=0.8,en-US;q=0.6,hu;q=0.4',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'cdn-api.co-vin.in',
    'User-Agent': 'request',
    # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}


# loading environment
load_dotenv()

# For telegram feature
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
USERID = os.getenv('USERID')
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# To create a list of vaccines available
vaccine18 = {}
vaccine45 = {}
num = 0

# Named it oneDistrict beacause it only checks the availability in ne district. Was planning to expand it to all
# districts in kerala


def oneDistrict():
    global num
    try:
        # For getting the date in our format
        x = datetime.datetime.now()
        t = []
        t.append(x.strftime("%d"))
        t.append(x.strftime("%m"))
        t.append(x.strftime("%Y"))
        date = "-".join(t)

        # To det the district
        districtCode = '303'

        # URL with district code and date (list of all district codes are listed at the bottom of code)
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+districtCode+"&date="+date
        response = requests.get(url, headers=headers)
        # print(response.text)
        data = response.json()

        vaccine18 = {}
        vaccine45 = {}

        if data == []:
            print("Nothing available")

        for center in data['centers']:
            centerName = center['name']
            pincode = center['pincode']
            for session in center['sessions']:
                availableCap = session['available_capacity']
                dateAvailable = session['date']
                if session['min_age_limit'] == 45:
                    # print("Vaccine for 45+ available at "+centerName)
                    if centerName in vaccine45:
                        vaccine45[centerName] += 1
                    else:
                        vaccine45[centerName] = 1

                else:
                    # print("Vacccine for 18+ available at "+centerName)
                    if centerName in vaccine18:
                        vaccine18[centerName] += 1
                    else:
                        vaccine18[centerName] = 1

        # if not bool(vaccine45):
        #     pass

        # else:
        #     # sti = ','.join(vaccine45.keys())
        #     # bot.send_message(chat_id=USERID, text="Vaccine for 45+ available at " +
        #     #                  sti+" ("+str(len(vaccine45.keys()))+" locations)")
        #     pass

        if not bool(vaccine18):
            # bot.send_message(
            #     chat_id=USERID, text="Vaccine not available for 18+")
            pass

        else:
            sti = ','.join(vaccine18.keys())
            bot.send_message(chat_id=USERID, text="Vaccine for 18+ available at " +
                             sti+" ("+str(len(vaccine18.keys()))+" locations)")

        print(num, " : ", datetime.datetime.now())
        print("----------------18+-----------------")
        print(*vaccine18.keys(), sep=", ", end="\n")
        print("----------------45+-----------------")
        print(*vaccine45.keys(), sep=", ", end="\n\n")

        num += 1

    except Exception as e:
        # For sending the error in code to telegram
        print(e)
        bot.send_message(chat_id=USERID, text=str(e))


def workingCheck():
    bot.send_message(chat_id=USERID, text="Vaccine checker working perfectly!")
    print("-----------WORKING PERFECTLY-----------", num)


oneDistrict()
workingCheck()
schedule.every(2).minutes.do(oneDistrict)
schedule.every().hour.do(workingCheck)
schedule.every().day.at("08:00").do(workingCheck)
schedule.every().day.at("16:00").do(workingCheck)
schedule.every().day.at("23:00").do(workingCheck)

while True:
    schedule.run_pending()
    time.sleep(1)


# https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=512&date=31-03-2021
# https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=303&date=01-05-2021

# districts = {301: 'alappuzha',
#              307: 'ernakulam',
#              306: 'idukki',
#              297: 'kannur',
#              295: 'kasaragod',
#              298: 'kollam',
#              304: 'kottayam',
#              305: 'kozhikode',
#              302: 'malappuram',
#              308: 'palakkad',
#              300: 'pathanamthitta',
#              296: 'thiruvananthapuram',
#              303: 'thrissur',
#              299: 'wayanad'
#              }
