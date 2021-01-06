digits=list(map(str, *input().split()))
if len(digits):
    for i in range (0,len(digits)-2):
            if digits[i]==digits[i+1]:
                digits.pop(i)
                digits.pop(i)
    print(''.join(digits))
else:
    print('-1')