from time import time

start_script = time()

input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
answer = 0
count = 0
measurement = 0

for n in input_lines:
    n = int(n)
    count += 1
    if count == 1:
        measurement = n
    else:
        if n > measurement:
            answer += 1
    measurement = n

print(f'Answer is: {answer}')

end_script = time()

total_time = end_script - start_script
print(f'Program takes {round(total_time, 2)} sec.')
