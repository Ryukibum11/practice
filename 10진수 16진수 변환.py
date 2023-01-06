#5 십진수를 16진수로 바꾸기
num = 200
bin_num = ''
while num > 0:
    if str(bin_num) == '10':
        bin_num = 'A'
    elif str(bin_num) == '11':
        bin_num = 'B'
    elif str(bin_num) == '12':
        bin_num = 'C'
    elif str(bin_num) == '13':
        bin_num = 'D'
    elif str(bin_num) == '14':
        bin_num = 'E'
    elif str(bin_num) == '15':
        bin_num = 'F'
    bin_num = str(num % 16) + bin_num
    num = num // 16
print(bin_num)
