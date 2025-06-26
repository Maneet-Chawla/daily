def fibonacci_series(n): #using a for loop (iterative)1
    a,b = 0,1
    for _ in range(n):
        print(a, end=" ")
        a,b =b, a+b

fibonacci_series(10) #First 10 terms
