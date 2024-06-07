

def check_palindrome(n:int):
    if str(n)==str(n)[::-1]:
        return True
    return False

def largest_palindrome_product(n_digits):
    start = 10**(n_digits-1)
    end = 10**n_digits - 1
    largest_palindrome = 0
    for i in range(end, start-1, -1):
        for j in range(i, start-1, -1):
            product = i * j
            if check_palindrome(product) and product>largest_palindrome:
                largest_palindrome = product
    return largest_palindrome

print(largest_palindrome_product(3))