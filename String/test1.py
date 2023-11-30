#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(string, k):
    length = len(string)

    for i in range(0, length, k):
        res = ""
        substring = string[i:i+k]

        for c in substring:
            if c not in res:
                res = res + c

        print(res)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
