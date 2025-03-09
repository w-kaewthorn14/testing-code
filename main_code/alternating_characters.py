def alternatingCharacters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        print(alternatingCharacters(s))
