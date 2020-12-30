"""
https://vijos.org/p/1103
校门外的树
"""
if __name__ == "__main__":
    l_str, m_str = input().split()
    L = int(l_str)
    M = int(m_str)
    L_list = [0] * (L + 1)
    cut_count = 0
    cut = 0
    for i in range(M):
        start, end = [int(n) for n in input().split()]
        L_list[start-1] += 1
        L_list[end-1] += -1
    for tree in L_list:
        cut += tree
        if cut or tree == -1:
            cut_count += 1
    print(L-cut_count)
