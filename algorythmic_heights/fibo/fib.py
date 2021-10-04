
def fib_n(n):
    fib_prev = 0
    fib_cur = 1

    for _ in range(0, n - 1):
        tmp = fib_cur + fib_prev
        fib_prev = fib_cur
        fib_cur = tmp
    return fib_cur

if __name__ == "__main__":
    z = []
    max_vertex = 0
    with open("rosalind_fibo.txt") as f:
        for line in f:
            fibn = int(line.strip())
    if fibn == 0:
        print("0")
    else:
        des_num = fib_n(fibn)
        print(des_num)

