# Train_Alert

This python project gets real time train information from the RTT API so you can be alerted of your train platform.

You input your train route and time and it will find the correct service and notify you when the platform for it is confirmed.

To run this code, create a RTT account at https://api.rtt.io/ and update the username and password in Train.py.
The project uses Twilio to send alerts, sign up at Twilio and update the SID, Auth token and from number in Train.py

Then run the code with "python main.py", it will ask for input for starting station, end destination and the time/date of the train. 
It calls the API and finds the closest train to your time, then checks if the platform is confirmed and sends you an alert.
