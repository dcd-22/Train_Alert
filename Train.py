import requests
import json
from twilio.rest import Client



username = "enter username"
password = "enter password"

account_sid = "enter Twilio Account sid"
auth_token = "enter Twilio Auth token"



class Train:
    def __init__(self,start,end,day,month,time):
        self.start = start
        self.end = end
        self.day = day
        self.month = month
        self.time = time
        self.service_id = self.get_serviceid()
        self.platform_confirmed = False
        self.platform = self.get_platform()


    def __str__(self):
        return f"Starting Destination {self.start}, \nEnd Destination {self.end}, \nTime of train: {self.time},\nPlatform {self.platform}"

    def send_text(self):
        if self.platform_confirmed == True:
            client = Client(account_sid, auth_token)
            client.messages.create(
            body = (f"Your train platform has been confirmed and is {self.platform_number}"),
            from_ = "[+][1][000000000]",# Your Twilio number
            to = "[+][1][00000000]")


    def get_serviceid(self):
        api_request = (f"http://api.rtt.io/api/v1/json/search/{self.start}/to/{self.end}")
        r = requests.get(api_request, auth=(username, password))
        data = json.loads(r.text)
        services = data["services"]
        serviceid = "NO_TRAIN"

        for train in services:
            time = int(train["locationDetail"]["gbttBookedDeparture"])
            if time >= (int(self.time)-5) and time <= (int(self.time)+5):
                serviceid = (train["serviceUid"])
                self.time = time
        return serviceid

    def get_platform(self):
        if self.service_id == "NO_TRAIN":
            platform = "NO_PLATFORM"
            return platform
        else:
            api_request2 = (f'http://api.rtt.io/api/v1/json/service/{self.service_id}/2022/{self.month}/{self.day}')
            r2 = requests.get(api_request2, auth=(username, password))
            train_data = json.loads(r2.text)
            locations = train_data["locations"]

            for i in locations:
                if self.start == i["crs"]:
                    platform_number = i["platform"]
                    self.platform_confirmed = i["platformConfirmed"]
                    return (f"{platform_number}, Platform Confirmed: {self.platform_confirmed}")



