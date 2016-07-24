def palindromic(string):
    halflen=len(string)/2
    if string[:halflen]==string[-halflen:][::-1]:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    print palindromic(raw_input())
