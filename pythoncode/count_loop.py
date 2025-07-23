# 简单的循环计数程序
def count_to_n(n):
    for i in range(1, n + 1):
        print(f"Count: {i}")
    return n

if __name__ == "__main__":
    count_to_n(5)