#It doesnt occupy the memory and can handle a lare data very easily as below.
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']



def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

t1 = time.clock()
people = people_list(1000000000)
for each in people:
    print(each)
t2 = time.clock()

# t1 = time.clock()
# people = people_generator(1000000000)
# for i in range(1000000000):
#     print(next(people))
# t2 = time.clock()



print ('Took {} Seconds'.format(t2-t1))