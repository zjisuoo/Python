class Person():
    def __init__(self, age):
        self.age = age

fab = Person(age = 42)

id(fab)
id(fab.age)
fab.age = 25 # I wish!
id(fab) # will be the same
id(fab.age) # will be different