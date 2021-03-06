# COVID VACCINE 18+ CHECKER WITH TELEGRAM NOTIFIER
Hello again,
This app is for checking the cowin site if vaccine for 18+ is available in the centers. All details regarding vaccine will be sent to your telegram every 2 minutes.

Timings and code can be changed according to your needs.

With simple modifications, you can change this to 
- Get daily availability
- Search by state
- Search by district

This whole project can be deployed in heroku easily so that it can run 24x7.

## HOW IT WORKS
It accesses the public API of COWIN for getting information regarding the vaccine.
The app is really simple. Data from API is recieved in JSON format and we just filter this data and creates some loops where if the min age limit is 18, telegram notifications are to be sent.

By varying parameters like district and date, you can get different data in JSON format. Try the given link by changing to todays date in your browser and see the data.
To get vaccination details for a single day for a district:
#### `https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=512&date=31-03-2021`

To get vaccine details for an entire week for a district:
#### `https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=303&date=01-05-2021`

Similarly you can find many requests and all these can be found below.

For more details about API visit [here](https://apisetu.gov.in/public/marketplace/api/cowin)

## INFORMATION ABOUT EACH FILES
- `.vscode`          : It is irrelevant and contains which python.exe should be run in my PC
- `.env`             : It should contain `TELEGRAM_TOKEN` and `USER_ID` for working. Details are given below
- `.gitignore`       : It has the content .env because .env contains all my tokens which should be private. So all the files mentioned inside .gitignore won't be uploaded to github. [More details](https://git-scm.com/docs/gitignore)
- `looper.py`        : This is the main code file
- `Procfile`         : The procfile is for heroku. Procfile should contain the name of the file that heroku should run in their servers.[More details](https://devcenter.heroku.com/articles/procfile)
- `requirements.txt` : It contains all the modules we have to install for running the code locally as well as in heroku. But while deploying in heroku, after pushing, heroku itself will install all the modules inside requirements file
- `README.md`        : You know what this is.

## WHAT YOU HAVE TO DO

- You have to create a telegram bot and get the `TELEGRAM_TOKEN` and `USER_ID`. `USER_ID` here is the chat ID. [How to make a telegram bot](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e).
- If you want to make a telegram group and notify all your friends then get the `GROUP_ID`. [Get group ID here](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)
- Then create a .env file in this same directory and set `TELEGRAM_TOKEN` and `USER_ID`.
- If you are in KERALA, all the district IDs are commented in the code itself. So make changes in the `districtCode` and voila!
- If you are not in KERALA, you have to first get the state code. I got the codes by visiting [here](https://cdn-api.co-vin.in/api/v2/admin/location/states). The result is printed below so you dont have to.
```{
    "states": [
        {
            "state_id": 1,
            "state_name": "Andaman and Nicobar Islands"
        },
        {
            "state_id": 2,
            "state_name": "Andhra Pradesh"
        },
        {
            "state_id": 3,
            "state_name": "Arunachal Pradesh"
        },
        {
            "state_id": 4,
            "state_name": "Assam"
        },
        {
            "state_id": 5,
            "state_name": "Bihar"
        },
        {
            "state_id": 6,
            "state_name": "Chandigarh"
        },
        {
            "state_id": 7,
            "state_name": "Chhattisgarh"
        },
        {
            "state_id": 8,
            "state_name": "Dadra and Nagar Haveli"
        },
        {
            "state_id": 37,
            "state_name": "Daman and Diu"
        },
        {
            "state_id": 9,
            "state_name": "Delhi"
        },
        {
            "state_id": 10,
            "state_name": "Goa"
        },
        {
            "state_id": 11,
            "state_name": "Gujarat"
        },
        {
            "state_id": 12,
            "state_name": "Haryana"
        },
        {
            "state_id": 13,
            "state_name": "Himachal Pradesh"
        },
        {
            "state_id": 14,
            "state_name": "Jammu and Kashmir"
        },
        {
            "state_id": 15,
            "state_name": "Jharkhand"
        },
        {
            "state_id": 16,
            "state_name": "Karnataka"
        },
        {
            "state_id": 17,
            "state_name": "Kerala"
        },
        {
            "state_id": 18,
            "state_name": "Ladakh"
        },
        {
            "state_id": 19,
            "state_name": "Lakshadweep"
        },
        {
            "state_id": 20,
            "state_name": "Madhya Pradesh"
        },
        {
            "state_id": 21,
            "state_name": "Maharashtra"
        },
        {
            "state_id": 22,
            "state_name": "Manipur"
        },
        {
            "state_id": 23,
            "state_name": "Meghalaya"
        },
        {
            "state_id": 24,
            "state_name": "Mizoram"
        },
        {
            "state_id": 25,
            "state_name": "Nagaland"
        },
        {
            "state_id": 26,
            "state_name": "Odisha"
        },
        {
            "state_id": 27,
            "state_name": "Puducherry"
        },
        {
            "state_id": 28,
            "state_name": "Punjab"
        },
        {
            "state_id": 29,
            "state_name": "Rajasthan"
        },
        {
            "state_id": 30,
            "state_name": "Sikkim"
        },
        {
            "state_id": 31,
            "state_name": "Tamil Nadu"
        },
        {
            "state_id": 32,
            "state_name": "Telangana"
        },
        {
            "state_id": 33,
            "state_name": "Tripura"
        },
        {
            "state_id": 34,
            "state_name": "Uttar Pradesh"
        },
        {
            "state_id": 35,
            "state_name": "Uttarakhand"
        },
        {
            "state_id": 36,
            "state_name": "West Bengal"
        }
    ],
    "ttl": 24
}
```

- Then copy the URL given below to a browser and change the state ID to yours and get your desired district codes.
`https://cdn-api.co-vin.in/api/v2/admin/location/districts/17` -- (Change the 17 to your state code from above and get all the district codes. And then copy your desired district code and then make changes to `looper.py` voila!)

## HOW TO DEPLOY TO HEROKU
> You need to first install the Heroku CLI and search about HEROKU. Heroku is a platform where you can host your codes so that it will run 24x7 free of cost. 

**Deployment**
 1. `git clone https://github.com/plal99/CoWIN-notifier`
 2. `cd CoWIN-notifier`
 3. `pip install -r requirements.txt`
 4. Now through Heroku-CLI login to your Heroku account. 
 `heroku login -i`
 5. Create a Heroku App `heroku create appname --buildpack heroku/python`
 6. You need to set your timezone on Heroku. `heroku config:add TZ="Asia/Kolkata"` change it to your timezone by using TZ="Your timezone". For India it is TZ="Asia/Kolkata"

 7. Initialize git repository  `git init`
 8. Select this app in your Heroku-CLI `heroku git:remote -a appname`
 9. Add all files to `git add .`
 10. Commit the changes `git commit -am "Your commit message"`
 11. Push Code to Heroku `git push heroku master`
 12. Scale the dynos `heroku ps:scale worker=1`