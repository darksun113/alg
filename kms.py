

next = [-1,0,0,0,0,0,0]
pattern = "ABCDABD"
target = "BBC ABCDAB ABCDABCDABDE"

def force_search(pat, text):
    N = len(pat)
    M = len(text)
    round = 0
    i = 0
    j = 0
    end = M - N
    for i in range(0,end) :
        for j in range(0, N) :
            print("Force: i={0},j={1},'{2}','{3}', Round={4}".format(i,j,text[i],pat[j],round))
            round += 1
            if(text[i+j]!=pat[j]):
                break
        if(j==N):
            #print("Force search need {0} rounds.".format(round))
            return i
    #print("Force search need {0} rounds.".format(round))
    
    return -1

def cal_next(pat, next):
    N = len(pat)
    k = -1
    j = 0
    round = 0
    while (j<N-1):
        if(k==-1 or pat[k]==pat[j]):
            j = j+1
            k = k+1
            next[j] = k
        else:
            k = next[k]
        #print("Round {0}: next={1}".format(round, next))
        round = round + 1

def kms_search(text, pat, next):
    M = len(text)
    N = len(pat)
    i = 0
    j = 0
    round = 0
    while (i < M and j < N):
        print("KMS: i={0},j={1},'{2}','{3}', Round={4}".format(i,j,text[i],pat[j],round))
        #print("Round {0}: j={1}, i={2}, text[i]={3}, pat[j]={4}".format(round,j,i,text[i],pat[j]))
        if(j==-1 or text[i] == pat[j]):
            i = i+1
            j = j+1
        else:
            #print("Round {0}: j={1}, i={2}, j is updated to next[j]: {3}".format(round,j,i,next[j]))
            j = next[j]
        round = round + 1
    if (j == N):
        return i - j
    else:
        return -1

force_search(pattern,target)
cal_next(pattern,next)
kms_search(target,pattern,next)