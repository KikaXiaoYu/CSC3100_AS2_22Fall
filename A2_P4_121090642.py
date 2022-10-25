
# global var
g_num = int()
g_oper_lst = list()
g_para_lst = list()
g_lst = list()

def doOperOne(p_lst, p_para_lst):
    pos = p_para_lst[0]
    value = p_para_lst[1]
    p_lst.insert(pos, value)

def doOperTwo(p_lst, p_para_lst):
    pos = p_para_lst[0]-1
    del p_lst[pos]

def doOperThr(p_lst, p_para_lst):
    start = p_para_lst[0]-1
    end = p_para_lst[1]-1
    ele_sum = 0
    for i in range(start, end+1):
        ele_sum += p_lst[i]
    print(ele_sum)

# the main
if (__name__ == "__main__"):
    g_num = int(input())
    g_lst = list()
    for i in range(g_num):
        g_oper_lst = [int(i) for i in input().split()]
        g_para_lst = g_oper_lst[1:]
        if g_oper_lst[0] == 1:
            doOperOne(g_lst, g_para_lst)
        if g_oper_lst[0] == 2:
            doOperTwo(g_lst, g_para_lst)
        if g_oper_lst[0] == 3: 
            doOperThr(g_lst, g_para_lst)

