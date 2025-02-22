my_dict = {}
my_dict={1: 'apple', 2: 'Banana'}
my_dict={'name': 'Atharv', 'age':15}
print(my_dict['name'])
print(my_dict['age'])
my_dict['age']=16
print(my_dict)
my_dict['address']='Downtime'
print(my_dict)
my_dict.pop('address')
print(my_dict)
print("address:", mu_dict.get('address'))
print("Name:", my_dict.get('name'))
my_dict.clear()
print(my_dict)