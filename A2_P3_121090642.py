
# global var
g_k = int()
g_size = int()
g_idx_lst = list()

# get the idx from row, col, and global g_size
def getIdx(p_row, p_col):
    global g_size
    idx = p_row*g_size + p_col
    return idx

# print the carpet
def printCarpet(p_size, p_idx_lst):
    for row in range(p_size):
        for col in range(p_size):
            print(p_idx_lst[getIdx(row, col)], end="")
        print()

# remove the area recursively
def removeArea(p_start_row, p_start_col, p_cur_size, p_idx_lst):
    # get the size to remove, also for the next recursion's current size
    cur_rm_size = int (p_cur_size / 3)
    # remove the area during start-idx and cur_rm_size
    col = p_start_col + cur_rm_size
    for i in range(cur_rm_size):
        row = p_start_row + cur_rm_size + i
        idx = getIdx(row, col)
        p_idx_lst[idx : idx+cur_rm_size] = [" " for _ in range(cur_rm_size)]
    # if next_size > 1, then we need further recursion
    next_size = cur_rm_size
    if (next_size > 1):
        for next_row in range( # get next_rows
            p_start_row,
            p_start_row + 2*next_size+1,
            next_size
            ):
            for next_col in range( # get next_cols
                p_start_col,
                p_start_col + 2*next_size+1,
                next_size
                ):
                removeArea(next_row, next_col ,next_size, p_idx_lst)
    else:
        return None

# the main
if (__name__ == "__main__"):
    g_k = int(input())
    g_size = 3**g_k
    g_idx_lst = ["#" for i in range(g_size**2)]
    removeArea(0, 0, g_size, g_idx_lst)
    printCarpet(g_size, g_idx_lst)
