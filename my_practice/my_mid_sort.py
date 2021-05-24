import random as rn

"""Mid sort

"""
def find_mid(a,b,c,a_list):
    temp = [a_list[a],a_list[b],a_list[c]]
    temp.sort()
    return temp[1]

def mid_sort(a_list, left, right):
    length = len(a_list)
    l_pivot = a_list[left]
    r_pivot = a_list[right]
    l_array = []
    m_array = []
    r_array = []
    
    if length < 3:          # Not enough elements to determine mid
        return a_list

    for i in range(1, length - 1):              # Categorizing each elemnt
        mid = find_mid(left, i, right, a_list)
        if mid == l_pivot:
            l_array.append(a_list[i])
        elif mid == a_list[i]:
            m_array.append(a_list[i])
        elif mid == r_pivot:
            r_array.append(a_list[i])

    l_array.append(a_list[left])    # send new pivot to next itereation
    m_array.append(a_list[right])
    r_array.insert(0, r_pivot)  # special cases for right array
    print("states:",l_array, m_array, r_array)

    if len(l_array) > 2:            
        l_array = mid_sort(l_array, 0, -1)
    if len(m_array) > 2:
        m_array = mid_sort(m_array, 0, -1)
    if len(r_array) > 2:
        r_array = mid_sort(r_array, 0, -1) 
    print(l_array + m_array + r_array[1:])

    return l_array + m_array + r_array[1:]   

if __name__ == "__main__":
    # test = [rn.randint(0,10) for _ in range(60)]
    test = [8,2,4,9,6,8]
    print("Origin:", test)
    print("After:",mid_sort(test,0, -1))

