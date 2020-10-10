def rec_fibo(n):
    #Fibonacci Series
    if n<=1:
        return n
    else:
        return(rec_fibo(n-1)+rec_fibo(n-2))

nTerms=int(input("Upto how many numbers do you want to see the Fibonacci Series "))
if nTerms<=0:
    print("Enter a postive number - Upto how many numbers do you want to see the Fibonacci Series ")
else:
    print("Fibonacci Series")
    for i in range(nTerms):
        print(rec_fibo(i))
