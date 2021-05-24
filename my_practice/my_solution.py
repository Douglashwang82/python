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
        # mid = find_mid(left, i, right, a_list)
        mid = ask(a_list[left], a_list[i], a_list[right])
        if mid == l_pivot:
            l_array.append(a_list[i])
        elif mid == a_list[i]:
            m_array.append(a_list[i])
        elif mid == r_pivot:
            r_array.append(a_list[i])

    l_array.append(a_list[left])    # send new pivot to next itereation
    m_array.append(a_list[right])
    r_array.insert(0, r_pivot)  # special cases for right array
    if len(l_array) > 2:            
        l_array = mid_sort(l_array, 0, -1)
    if len(m_array) > 2:
        m_array = mid_sort(m_array, 0, -1)
    if len(r_array) > 2:
        r_array = mid_sort(r_array, 0, -1) 

    return l_array + m_array + r_array[1:]   

def ask(a,b,c):
    print(a,b,c)
    respond = input()
    return int(respond)

if __name__ == "__main__":
    case_input = input()
    case_input = case_input.split(" ")
    T = int(case_input[0])
    N = int(case_input[1])
    Q = case_input[2]
    
    while T > 0:
        r = [i for i in range(1, N + 1)]
        sordted = mid_sort(r, 0, -1)
        
        print(*sordted)
        
        responad = input()
        T -= 1
        