from faker import Faker

myfake = Faker('ko_KR')

myfake.seed()
print(myfake.name())
print(myfake.address())
#print(myfake.text())
#print(myfake.state())
#print(myfake.sentences())
print(myfake.random_number())

