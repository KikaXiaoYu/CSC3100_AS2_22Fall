
# global var


g_num = int()

# get binary power representation in list form
def getBiPowLst(p_num):
    # variables
    bi_lst = list()
    cur_num = p_num
    # get reverse binary list
    # e.g. 137 -> [1, 0, 0, 1, 0, 0, 0, 1]
    while (cur_num >= 1):
        reminder = int(cur_num % 2)
        cur_num = int(cur_num // 2)
        bi_lst.append(reminder)
    # get power list
    # e.g. 137 -> [7, 3, 0]
    pow_lst = list()
    for i in range(len(bi_lst)-1, -1, -1):
        if (bi_lst[i] == 1):
            pow_lst.append(i)
    # return the power list
    return pow_lst

# get 02 representation
def getZeroTwo(p_num):
    # variables
    cur_lst = getBiPowLst(p_num)
    new_str = str() # the str result for p_num
    bracket = bool() # whether add a bracket
    # evaluate each number in the power list
    for i in range(len(cur_lst)):
        cur_num = cur_lst[i]
        # check whether 02 form
        if (cur_num not in [0, 1, 2]): # if not, further recursion
            cur_str = getZeroTwo(cur_num)
            bracket = True
        else: # if yes, get the str form for cur_num
            cur_str = ["2(0)","2","2(2)"][cur_num]
            bracket = False
        # add the str form together following rules
        if (i != 0): 
            new_str += "+" # add sgn for more elements
        if (bracket == True): # two or more elements for cur_str
            new_str += "2("+cur_str+")"
        else: # single element for cur_str
            new_str += cur_str
    # return the str result
    return new_str

# the main
if (__name__ == "__main__"):
    g_num = int(input())
    print(getZeroTwo(g_num))

