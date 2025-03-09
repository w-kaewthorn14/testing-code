import os  # Add this import statement to use os.environ

def funnyString(s):
    n = len(s)
    # Iterate through the string and compare the differences in ASCII values
    for i in range(1, n):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s[n-i]) - ord(s[n-i-1])):
            return "Not Funny"
    return "Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # This requires the os module

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()