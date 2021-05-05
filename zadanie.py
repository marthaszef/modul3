"""
a = 1

def scope_demo():
    a = 2
    print(a)

scope_demo()
print(a)
print(type(None))
help(print())
def customized_hello(first_name, last_name, gender_prefix='Mr'):
    """
        Prints hello, based on arguments passed
        Arguments:
        first_name,
        last_name
        Optional arguments:
        gender_prefix:  Mr/Ms based on sex of person
    """

print("Hello %s %s %s" % (gender_prefix, first_name, last_name))
help(customized_hello())
"""
n=5
for i in range(n,0,-1):
	    for j in range(i):
	        print('* ', end="")
	    print('')