"""
4柱子汉诺塔
https://vijos.org/p/1073

n个盘子从1到4可以拆解为
1.将n-1个盘子放在中间两个柱子上
2.将最大盘从1移到4
3.将n-1个盘子从中间移到4号

1.1 n-1个盘子移动到中间两根柱子，可以拆解为第n-2个盘子移到中间
1.2 n-1大盘子从1到4
1.3 n-2个盘子从2到4 {}
1.4 n-1大盘子从4到2
"""


def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    return 2 * f(n//2) + f3(n-n//2) # n//2不一定是分界点，随着n越大，分界点将越大


def f3(m):
    if m == 0:
        return 0
    if m == 1:
        return 1
    if m == 2:
        return 3
    return 2 * f3(m-1) + 1


if __name__ == "__main__":
    n = int(input())
    re_n = []

    print(f(n) % 10000)
