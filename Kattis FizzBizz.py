

# FizzBuzz
# https://open.kattis.com/problems/fizzbuzz


fizz,buzz,total= map(int, input().split(' '))

for i in range(1,total+1):
    if i%fizz == 0 and i%buzz == 0:
        print('FizzBuzz')
    elif i%fizz == 0:
        print('Fizz')
    elif i%buzz == 0:
        print('Buzz')
    else:
        print(i)















