my_dict={'Alex':1999,'Oleg': 2000,'Lexa': 2001}
print(my_dict)
print(my_dict.get('Alex'))
print(my_dict.get('kamila'))
my_dict={'Alex':1999,'Oleg': 2000,'Lexa': 2001,'Olesy':2002,'Igor':2004}
a=my_dict.pop('Oleg')
print(my_dict)
print(a)
my_set={4,5,6,7,3,4,5,6,7}
print(my_set)
my_set={4,5,6,7,3,4,5,6,7,'Soul',(1,2,4)}
print(my_set)
(my_set.discard('Soul'))
print(my_set)
