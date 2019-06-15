'''
Coding-eric video 13
Funciones pt2
'''
'''
Coding-eric video 13
Funciones pt2
'''
def suma(a,b):
	return a+b
def res(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b


def argumentos(*patitos):
	print(patitos)

def kwargumentos(**kwpatitos):
	print(kwpatitos)

op = {
	"suma": suma,
	"resta": res,
	"mul": mul,
	"div": div,
}

print(op["div"](12,3))

def change_var(v, l=[]):
	l.append(v)
	return l

change_var(2)
change_var(5)
change_var(6)
lst_2 = change_var(8)
print(lst_2) 
