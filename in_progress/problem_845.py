from tqdm import tqdm

def sum_of_digits_efficient(number):
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    return digit_sum

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False
    return [num for num in range(limit + 1) if primes[num]]

def D_optimized_efficient(limit):
    primes = set(sieve_of_eratosthenes(2000))  # Precompute primes up to a limit
    count = 0
    number = 1
    with tqdm(total=limit) as pbar:
        while count < limit:
            digit_sum = sum_of_digits_efficient(number)
            if digit_sum in primes:
                count += 1
                pbar.update(1)  # Update the progress bar
            number += 1
    return number - 1

# Example usage
result = D_optimized_efficient(10**16)
print(f"D(10^16) = {result}")
