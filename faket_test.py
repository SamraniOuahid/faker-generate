from faker import Faker 
import sys

# Set UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')
f = Faker("fr") 

for x in range(2):
    print("\n*********************\n")

# name
    # print("الاسم: "+ f.name_male())
    # print("username: "+ f.user_name())
    # print("first name: "+ f.first_name_male())
    # print("last name: "+ f.last_name_male())

#email
    # print("email:  "+ f.email())
    # print("free email:  "+ f.free_email())
    # print("company email:  "+ f.company_email())
    

# adress 
    # print("address: " + f.address())
    # print("country: "+ f.country())
    # print("current country: "+ f.current_country())
    # print("city: "+ f.city())
    # print("street: "+ f.street_name())
    # print("buildin number: "+ f.building_number())
    # print("postcode: "+ f.postcode())

#job 
    print("company name: " +f.company())
    print("company slogen: " +f.bs())
    print("company job: " +f.job())

#profile   
    # pro = f.simple_profile()
    # for key in pro:
    #     print(f"{key}: {pro[key]}")

