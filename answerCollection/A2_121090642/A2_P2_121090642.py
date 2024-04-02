
# global var
g_num = int()
g_point_lst = list()

# merge the seperated block
def merge(p_point_lst, p_tmp_lst, p_lstart, p_rstart, p_rend):
    lpos = p_lstart # left position
    rpos = p_rstart # right positiom
    lend = p_rstart-1 # left end
    rend = p_rend # right end
    tmp = lpos # tmp position
    inv_res = 0 # inverse number count
    # for both rest
    while (lpos <= lend and rpos <= rend):
        if (p_point_lst[lpos] < p_point_lst[rpos]):
            p_tmp_lst[tmp] = p_point_lst[lpos]
            tmp += 1
            lpos += 1
        else:
            p_tmp_lst[tmp] = p_point_lst[rpos]
            # it should be counted as an inverse pair
            inv_res += lend-lpos+1 
            tmp += 1
            rpos += 1
    # for left rest
    while (lpos <= lend):
        p_tmp_lst[tmp] = p_point_lst[lpos]
        tmp += 1
        lpos += 1
    # for right rest
    while (rpos <= rend):
        p_tmp_lst[tmp] = p_point_lst[rpos]
        tmp += 1
        rpos += 1
    # renew the p_point_lst
    for i in range(p_lstart, p_rend + 1):
        p_point_lst[i] = p_tmp_lst[i]
    # return the inv_res
    return inv_res

# do the mergeSort
def mergeSort(p_point_lst, p_tmp_lst, p_left, p_right):
    rev_res = 0
    if p_left < p_right:
        mid_point = (p_left + p_right) // 2
        rev_res += mergeSort(p_point_lst, p_tmp_lst, p_left, mid_point)
        rev_res += mergeSort(p_point_lst, p_tmp_lst, mid_point+1, p_right)
        rev_res += merge(p_point_lst, p_tmp_lst, p_left, mid_point+1, p_right)
    return rev_res

# get the max number of crossing
def getMaxCrossing(p_num, p_point_lst):
    res = mergeSort(p_point_lst, [None for _ in range(p_num)], 0, p_num-1)
    return res

# the main
if (__name__ == "__main__"):
    g_num = int(input())
    g_point_lst = [int(i) for i in input().split()]
    print(getMaxCrossing(g_num, g_point_lst))

    
