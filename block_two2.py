total_sum=0
count=0
while True:
    number=int(input("Введите отрицательное число"))
    if number > 0:
        break
    total_sum+=number
    count+=1
    if count >0:
        average=total_sum/count
        print("Среднее арефмитическое", average)
    else:
        print("Ошибка")