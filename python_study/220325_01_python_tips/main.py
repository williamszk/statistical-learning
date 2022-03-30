#%%
condition = True

if condition:
    x = 1
else:
    x = 2

print(x)

#%%
# ternary operator
condition = False
x = 1 if condition else 0
print(x)

#%%
num1 = 10000000000
num2 = 10000000

total = num1 + num2
print(total)

#%%
# this is a better way to write long integers...
num1 = 10_000_000_000
num2 = 10_000_000

total = num1 + num2
print(total)

# a better way to print the integer...
print(f"{total:,}")
# %%
# can we separte float?
num1 = 10_000_000_000.999
num2 = 10_000_000.111

total = num1 + num2
print(total)
# yes we can

# a better way to print the float...
print(f"{total:,}")
type(total)

#%%
# this is how we open a file and read the content
# of the file
file = open("test.txt", "r")

file_content = file.read()

file.close()

words = file_content.split(" ")
word_count = len(words)
print(word_count)

# this code use explicit close which can be bad
# and we say that this is code smell
# instead we can use a context manager

#%%
with open("test.txt", "r") as open_file:
    file_content = open_file.read()

print(file_content)

#%%
names = ["Alice", "Bob", "Eve", "Malory", "Oscar"]

index = 0
for name in names:
    print(index, name)
    index += 1


#%%
names = ["Alice", "Bob", "Eve", "Malory", "Oscar"]

for index, name in enumerate(names) :
    print(index, name)

#%%
names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]

for index, name in enumerate(names):
    hero = heroes[index]
    print(f"{name} is actually {hero}")

#%%
names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]

for name, hero in zip(names, heroes):
    print(f"{name} is actually {hero}")

#%%
names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]
universes = ["Marvel", "DC", "Marvel", "DC"]

for name, hero, universe in zip(names, heroes, universes):
    print(f"{name} is actually {hero} from {universe}")

#%%
# unpacking tuples and lists
items = (1,2)
print(items)

a, b = items
print(a, b)

# if we want to ignore a variable
a, _ = items
print(a)

#%%
a,b,c = (1,2)
# this will give an error

#%%
a,b,c = (1,2, 3, 4, 5, 6)
# this will also give an error

#%%
a, b, *c = (1,2, 3, 4, 5, 6)
# this works
print(a)
print(b)
print(c)
#%%
a, *b, c = (1,2, 3, 4, 5, 6)
# this also works
print(a)
print(b)
print(c)

# %%
*a, *b, c = (1,2, 3, 4, 5, 6)
# this will give an error

# %%
# this is a way to ignore the rest of the values
a, b, *_ = (1,2, 3, 4, 5, 6)
print(a)
print(b)
# %%
class Person():
    pass

person = Person()

# dynamically add attributes to a class
# can we do this in Java or Go, or C++?
person.first = "Corey"
person.last = "Schafer"

print(person.first)
print(person.last)

# %%
class Person():
    pass

person = Person()

first_key = "first"
first_value = "Corey"

# this is how we set the value of an attribute using the name as a variable
setattr(person, first_key, first_value)

print(person.first)

# to get the value of an attribute using the key as a variable
print(getattr(person, first_key) )

# %%
class Person():
    pass

person = Person()

personal_info = {"first":"Corey", "last": "Schafer"}

for attr, value in personal_info.items():
    setattr(person, attr, value)

for key in personal_info.keys():
    print(getattr(person, key))

# .items()
# .keys()
# .values()

# %%
# to include secret information into the program
# use environment variables
# or use secret files that are not commited

# %%
username = input("Username: ")
password = input("Password: ")

print("Logging in...")
# the problem here is that while typing the password
# the string will be displayed in the terminal...

# %%

from getpass import getpass
username = input("Username: ")
password = getpass("Password: ")
# this way the password will not be displayed
print("Logging in...")

# %%
import sys
print(sys.path)

# -m in the code "python -m"
# means that some one is running a module
# or script
# and the rest are argument that are used in the module

# %%
# how to find out more about a module

import smtpd
help(smtpd)

# Help on module smtpd:

# NAME
#     smtpd - An RFC 5321 smtp proxy with optional RFC 1870 and RFC 6531 extensions.

# MODULE REFERENCE
#     https://docs.python.org/3.9/library/smtpd
    
#     The following documentation is automatically generated from the Python
#     source files.  It may be incomplete, incorrect or include features that
#     are considered implementation detail and may vary between Python
#     implementations.  When in doubt, consult the module reference at the
#     location listed above.

# DESCRIPTION
#     Usage: %(program)s [options] [localhost:localport [remotehost:remoteport]]
    
#     Options:
    
#         --nosetuid
#         -n
#             This program generally tries to setuid `nobody', unless this flag is
#             set.  The setuid call will fail if this program is not run as root (in
#             which case, use this flag).
    
#         --version
#         -V
#             Print the version number and exit.
    
#         --class classname
#         -c classname
#             Use `classname' as the concrete SMTP proxy class.  Uses `PureProxy' by
#             default.
    
#         --size limit
#         -s limit
#             Restrict the total size of the incoming message to "limit" number of
#             bytes via the RFC 1870 SIZE extension.  Defaults to 33554432 bytes.
    
#         --smtputf8
#         -u
#             Enable the SMTPUTF8 extension and behave as an RFC 6531 smtp proxy.
    
#         --debug
#         -d
#             Turn on debugging prints.
    

# %%
from datetime import datetime

dir(datetime)

# this is a list of all attributes and methods from the class
['__add__',
 '__class__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__radd__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rsub__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 'astimezone',
 'combine',
 'ctime',
 'date',
 'day',
 'dst',
 'fold',
 'fromisocalendar',
 'fromisoformat',
 'fromordinal',
 'fromtimestamp',
 'hour',
 'isocalendar',
 'isoformat',
 'isoweekday',
 'max',
 'microsecond',
 'min',
 'minute',
 'month',
 'now',
 'replace',
 'resolution',
 'second',
 'strftime',
 'strptime',
 'time',
 'timestamp',
 'timetuple',
 'timetz',
 'today',
 'toordinal',
 'tzinfo',
 'tzname',
 'utcfromtimestamp',
 'utcnow',
 'utcoffset',
 'utctimetuple',
 'weekday',
 'year']

datetime.today
# <function datetime.today>

# %%






