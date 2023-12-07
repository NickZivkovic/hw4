def my_steps(n):

    if n < 1 or n > 25:
        raise ValueError("integer not between 1 and 25.")
    else:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
    steps = [0] * (n + 1)
        
      
    steps[1] = 1
    steps[2] = 2
        
       
    for i in range(3, n + 1):
     steps[i] = steps[i - 1] + steps[i - 2]
    
    return steps[n]