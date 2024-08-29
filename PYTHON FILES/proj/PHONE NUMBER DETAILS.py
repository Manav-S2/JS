import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input('Enter Phone Number with +____: ')

phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
cr = carrier.name_for_number(phone, 'en')
reg = geocoder.description_for_number(phone, 'en')

print(phone)
print(time)
print(cr)
print(reg)


