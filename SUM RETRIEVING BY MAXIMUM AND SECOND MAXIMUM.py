def main():
    a = [1, 3, 8, 6, 7]
    max_num = 0
    smax_num = 0
    sum_max_smax = 0

    for num in a:
        if num > max_num:
            smax_num = max_num
            max_num = num
        elif num > smax_num and num != max_num:
            smax_num = num

    sum_max_smax = max_num + smax_num

    print(f"Maximum Number = {max_num}")
    print(f"Second maximum Number = {smax_num}")
    print(f"Sum of max and smax = {sum_max_smax}")

if __name__ == "__main__":
    main()
