# Path: python/two.py
def merge_sort(word1,word2):
    result = ""
    i,j = 0,0
    counter = 0
    while i < len(word1) and j < len(word2):
        if counter%2 ==0:
            result+=word1[i]
            i+=1
        else:
            result+=word2[j]
            j+=1
        counter+=1
    if i<len(word1):
        result+=word1[i:]
    if j<len(word2):
        result+=word2[j:]
    return result

def findTheDifference(s,t):
    t_dict = {}
    for i in t:
        if i in t_dict:
            t_dict[i]+=1
        else:
            t_dict[i]=1
    for i in s:
        if i in t_dict:
            t_dict[i]-=1
    for i in t_dict:
        if t_dict[i] == 1:
            return i
def strStr(s,t):
    if len(t)>len(s):return -1
    for i in range(len(s)-len(t)+1):
            if s[i:i+len(t)] == t:
                return i
    return -1


def isAnagram( s: str, t: str) -> bool:
        if len(s) != len(t):return False
        s_dict = {}
        for i in s:
            if i not in s_dict:
                s_dict[i] = 1
            else:
                s_dict[i]+= 1
        print(s_dict)
        for j in t:
            if j not in s_dict:
                return False
            else:
                s_dict[j]-=1
        print(s_dict)
        for i in s_dict:
            if s_dict[i] != 0:
                return False
        return True


def main():
    s,t = "aacc","ccac"
    print(s,t)
    result = isAnagram(s,t)
    print(result)

if __name__ == "__main__":
    main()
