
print ('temperature(c,f,k); mass(kg,o,pnd); volume(l,p,g); currency(RSD, USD, EUR)')

# temperature
c = 1.0
f = 38.0
k = 274.15

# mass
kg = 1.0
o = 35.273962
pnd = 2.204623

#volume
l = 1.0
p = 1.759754
g = 0.219969

#currency
RSD = 1.0
USD = 0.012
EUR = 0.0088


def unit_converter():
  while True:
    prompt = raw_input('>')
    t1, t2, val = prompt.split()
    print 1.0 * (int(val) / eval(t1)) * eval(t2)
    
unit_converter()