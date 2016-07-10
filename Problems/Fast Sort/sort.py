def mysort(alphabet):
    return ''.join(sorted(raw_input(), key=lambda word: [alphabet.index(c) for c in word[0]]))

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print mysort(raw_input())
