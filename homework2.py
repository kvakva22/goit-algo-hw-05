def generator_numbers(text):
    words = text.split()
    for word in words: 
        try:
            yield float(word)
        except ValueError:
            pass 

def sum_profit(text, func):
    sum = 0
    for word in func(text):
        sum += word
    return sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")