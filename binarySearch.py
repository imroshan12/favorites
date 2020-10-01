def bsearch(seq,v,l,r):
    if r-l == 0:
        return False
    mid = (l+r)//2
    if v == seq[mid]:
        return True
    if v < seq[mid]:
        return bsearch(seq,v,l,mid)
    else:
        return bsearch(seq,v,mid+1,r)
n = int(input())
li = list(map(int, input().split()))
print(bsearch(li,3,0,n))