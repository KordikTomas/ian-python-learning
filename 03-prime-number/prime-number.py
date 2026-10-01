
def is_prime(n):
    for i in range(2, n // 2 +1):
        if n % i == 0:
            return False
        
    return True

def verify_is_prime(n, expectedResult):
    actualResult = is_prime(n)
    if actualResult != expectedResult:
        print("Zastřelit Pandu, protože je to špatně")

verify_is_prime(6, False)
verify_is_prime(2, True)
verify_is_prime(10, False)
verify_is_prime(5, True)
verify_is_prime(16, False)
verify_is_prime(18, False)
verify_is_prime(20, False)
verify_is_prime(19, True)
verify_is_prime(22, False)
verify_is_prime(103, True)
