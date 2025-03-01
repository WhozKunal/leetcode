#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
#and two integers m and n, representing the number of elements in nums1 and nums2 respectively.


def merger_array(num1: list[int], m :int, num2 :list[int], n :int) -> None:
    print(m)
    print(n)
    
    i  = m -1
    print(i)
    j  = n -1 
    print(j)
    k  = m +n -1
    print(k)
    
    while i >= 0 and j >=0:
        if num1[i] > num2[j]:
            num1[k] = num1[i]
            i -= 1
            
        else:
            num1[k] = num2[j]
            j -= 1
        k -= 1
        
        
    while j >= 0:
        num1[k] = num2[j]
        j -= 1
        k -=1
        


    
