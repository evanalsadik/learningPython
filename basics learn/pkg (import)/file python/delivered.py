#cara 1
import pkgmodule as pkg

x = pkg.say_hello()

#cara 2
from pkgmodule import say_hello

x = say_hello
x()

#cara 3 (import semua)
from pkgmodule import *

x = say_hi
x()