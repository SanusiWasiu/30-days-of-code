def Average(string):
    list_of_string = list(string.split(" "))
    Total = 0
    for num in list_of_string:
        integer = int(num)
        Total += integer 
    
    print(Total/len(list_of_string))
Average("12 11 2 6 7 10")
