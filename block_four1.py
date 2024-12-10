numbers=[1,2,3,4,5,6,7,8,9]
oddnumbers=[num for num in numbers if num %2 !=0]
if oddnumbers:
    min_odd=min(oddnumbers)
    print("Наименьший нечетный элемент")
else:
    print("В списке нету нечетных")
    