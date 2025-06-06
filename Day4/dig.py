num=int(input())
while num > 9:
    sum_dig = 0
    num_str = str(num)
    for dig_char in num_str:
      sum_dig += int(dig_char)
      num = sum_dig
    print(num) 
