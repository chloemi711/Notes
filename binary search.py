def binarysearch(prime_num,find_num):
    length = len(prime_num)
    begin_num = 0
    end_num = length - 1
    while begin_num <= end_num:
        mid_num = int(begin_num + (end_num - begin_num))
        if prime_num[mid_num] < find_num:
            begin_num = mid_num + 1
        elif prime_num[mid_num] > find_num:
            end_num = mid_num - 1
        else:
            return mid_num
    return None


    
prime_num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
             59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
M = binarysearch(prime_num,13)
print(M)

        

        
