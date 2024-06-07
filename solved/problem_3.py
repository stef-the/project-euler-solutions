from tqdm import tqdm
import math
import random

def pollards_rho(n, max_iterations=1000):
    def pollard_rho_iteration(x, n):
        return (x**2 + 1) % n

    x = random.randint(1, n - 1)
    y = x
    d = 1
    count = 0

    while d == 1 and count < max_iterations:
        x = pollard_rho_iteration(x, n)
        y = pollard_rho_iteration(pollard_rho_iteration(y, n), n)
        d = math.gcd(abs(x - y), n)
        count += 1

    return d

def find_prime_factors_with_progress(n):
    prime_factors = set()

    # Handle 2 separately
    while n % 2 == 0:
        prime_factors.add(2)
        n //= 2

    # Use Pollard's rho algorithm with a progress bar
    with tqdm(total=100, desc="Factorization") as pbar:
        count = 0
        while n > 1 and count < 100:
            factor = pollards_rho(n)
            while n % factor == 0:
                prime_factors.add(factor)
                n //= factor
            pbar.update(1)
            count += 1

    # If n is a prime number greater than 2
    if n > 2:
        prime_factors.add(n)

    return prime_factors

# Example usage
N = 600851475143
result = find_prime_factors_with_progress(N)
print(result)
