import phonenumbers
from phonenumbers import timezone, geocoder, carrier

user_phone_number = input("Enter your Phonr Number with +91(For INDIA) : ")
phone_number = phonenumbers.parse(user_phone_number)
time = timezone.time_zones_for_number(phone_number)
service_provider = carrier.name_for_number(phone_number,"en")
registration_details = geocoder.description_for_number(phone_number,"en")

print("The details of the phone number :",phone_number ,"are as follows:" )
print("The standard time zone of the phone number is : ", time)
print("The name of the service provider is :", service_provider)
print("Loaction of the phone number is :",registration_details)