# COVID VACCINE 18+ CHECKER WITH NOTIFIER
Hello again,
This app is for checking the cowin site if vaccine for 18+ is available in the servers. You will get availability data for a week.

With simple modifications, you can change this to 
- Get daily availability
- Search by state
- Search by district

This whole project can be deployed in heroku easily

## HOW IT WORKS
It accesses the public API of COWIN for getting information regarding the vaccine.

The app is really simple. Data from API is recieved in JSON format and we just filter this data and creates some loops where if the min age limit is 18, telegram notifications are to be sent.

For more details about API visit [here](https://apisetu.gov.in/public/marketplace/api/cowin)

## WHAT YOU HAVE TO DO

- You have to create a telegram bot and get the `TELEGRAM_TOKEN` and `USER_ID`. `USER_ID` here is the chat ID. [How to make a telegram bot](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e).
- If you want to make a telegram group and notify all your friends then get the `GROUP_ID`. [Get group ID here](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)
- Then create a .env file in this same directory and set `TELEGRAM_TOKEN` and `USER_ID`.
- If you are in KERALA, all the district IDs are commented in the code. So make changes in the `districtCode` and voila!
- If you are not in KERALA, you have to get the district code and you can get that here