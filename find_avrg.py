def get_average(marks):
    
    # iterate through marks
    # average means size / total
    
    size = 0
    total = 0
    
    for i in marks:
        size += 1
        total += i
        
    avg = total / size
        
    return(avg)

print(get_average([5,6,3,2]))