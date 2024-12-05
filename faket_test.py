from faker import Faker # type: ignore

f = Faker() 
for x in range(10):
    print(f.name())
    print(f.address())
    print(f.email(), "\n******\n")


