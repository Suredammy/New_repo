def ero_prime():
    Dic = {}
    a = 2
    while a:
        if a not in Dic:
            yield a
            # The square of a prime number is added to the Dic, with the prime as value
            Dic[a * a] = [a]
        else:
            for b in Dic[a]:
                Dic.setdefault(b + a, []).append(
                    b
                )  # same as if b+a not in Dic: Dic[a+b] = [b],  else: Dic[a+b].append(b)
            del Dic[a]  # Deleted to free memory. No longer needed.
        a += 1


ero = ero_prime()
for i in range(20):
    print(next(ero))


def genPrimes():
    primes = [2]
    n = 3
    while n:
        check = True
        for i in primes:
            if n % i == 0:
                check = False
                break
        if check:
            primes.append(n)
            yield n
        n += 1


# primes = genPrimes()
# for i in range(10):
#     print(primes.__next__())
code = "***<>>.**[this[] is fun[]go fun it ]"
stack, bracket = [], {}
for i, c in enumerate(code):
    if c == "[": 
        stack.append(i)
    elif c == "]": 
        bracket[i] = stack[-1]
        bracket[stack.pop()] = i

print(stack, bracket)