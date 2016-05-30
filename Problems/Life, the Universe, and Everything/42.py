def stopat42():
    nums = []
    while True:
        i = raw_input()
        if i == '42':
            break
        else:
            nums.append(i)
    return nums

if __name__ == "__main__":
    nums=stopat42()
    for n in nums: print n
