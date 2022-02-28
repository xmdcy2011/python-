a = [i for i in range(10) if i % 2 == 0]
print(a)

my_dict = {'xx':1,'ss':3}
dict

b = {k for k,v in my_dict.items()}
print(type(b))
print(b)

c = {v:k for v,k in my_dict.items()}
print(c)