
from Train import Train
from dict import codes


starting_destination = input("Your Starting Destination Train Station ").lower()
end_destination = input("Your End Destination Station ").lower()
day_train = input("The day of your Train ")
month_train = input("The month of your Train ")
time_of_train = input("The Time of Your Train ")




start = codes[starting_destination]
end = codes[end_destination]

train = Train(start, end, day_train, month_train, time_of_train)
print(train.__str__())
train.send_text()
