def is_prime(n):
  for i in range (3,n,2):
    if n % i == 0 and n != i:
      return False
  return True

def next_prime():

  current = 3
  print '2'
  
  while True:
    prompt = raw_input('Do you want a next prime number?')
    if prompt == 'y':
      while is_prime(current) == False:
	current += 2
      print current
      current += 2
	
    elif prompt == 'n':
      break
    
    
next_prime()