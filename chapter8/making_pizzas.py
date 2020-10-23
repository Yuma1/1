#1
#import pizza
#2
#from pizza import make_pizza
#3
#from pizza import make_pizza as mp
#4
#import pizza as p
#5
from pizza import *

#1
#pizza.make_pizza('3', 'pepperroni')
#pizza.make_pizza('4', 'mushrooms', 'green peppers', 'extra cheese')

#2
#make_pizza('3', 'pepperroni')
#make_pizza('4', 'mushrooms', 'green peppers', 'extra cheese')

#3
#mp('3', 'pepperroni')
#mp('4', 'mushrooms', 'green peppers', 'extra cheese')

#4
#p.make_pizza('3', 'pepperroni')
#p.make_pizza('4', 'mushrooms', 'green peppers', 'extra cheese')

#5
make_pizza('3', 'pepperroni')
make_pizza('4', 'mushrooms', 'green peppers', 'extra cheese')
