def fibonacci(n):
  if(n<3):
    return 1 #ensures base case
  else:
    a = n
    lamp = range(3,a) # calling iteration to the nth number
    c = 1
    for s in lamp:
      if c != 1:
        f = d + c
        d = c
        c = f
        print("endres"+" "+ str(f))
      else:
        d = c + c
        e = d + c
        c = e
        
        print("C is"+ " "+ str(c))
        print("D is"+ " "+ str(d))
      
        


fibonacci(input)
