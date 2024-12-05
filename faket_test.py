from faker import Faker # type: ignore

f = Faker() 
for x in range(10):
    print("\n*********************\n")
    pro = f.simple_profile()
    for key in pro:
        print(f"{key}: {pro[key]}")

