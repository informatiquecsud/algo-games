from random import randint

def generate_random_numbers(a, size, distribution):
    values = []
    number_min = a
    count = 0
    for i, interval in enumerate(distribution):
        if i == len(distribution) - 1:
            numbers_to_generate = size - count
        else:
            numbers_to_generate = int(size / len(distribution))
            
        for _ in range(numbers_to_generate):
            number = randint(number_min, number_min + interval)
            values.append(number)
            number_min = number + 1
            count += 1
            
                        
    #print("values generated", values)

    return values
