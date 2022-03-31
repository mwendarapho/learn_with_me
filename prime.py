def is_prime(k):
    status=False 
    if k>1 and isinstance(k, int):
        for i in range(2,k+1):
            if k%i==0 and k!=i:
                status=False
                break
            else:
                status=True
    return status
