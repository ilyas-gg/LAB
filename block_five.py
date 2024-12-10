M = int(input("Введите число M: "))
N = int(input("Введите число N: "))


if M >= N:
    print("Число M не может быть больше или равно N")
else:
    def count_divisors(num):

        count = 0
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                count += 1 if i == num // i else
        return count

    def find_numbers_with_max_divisors(M, N):

        max_divisors = 0
        numbers_with_max = []

        for num in range(M, N + 1):
            divisors = count_divisors(num)
            if divisors > max_divisors:
                max_divisors = divisors
                numbers_with_max = [num]
            elif divisors == max_divisors:
                numbers_with_max.append(num)

        return numbers_with_max, max_divisors

    numbers, max_div = find_numbers_with_max_divisors(M, N)
    print(f"Числа с наибольшим количеством делителей ({max_div}) из интервала [{M}, {N}]: {numbers}")
