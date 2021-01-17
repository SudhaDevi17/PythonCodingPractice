def permute(s):
    out =[]
    if len(s)==1 :
        return s
    else:
        for i,num in enumerate(s):
            for perm in permute(s[:i]+s[i+1:]):
                out += [[num]+[perm]]

    return out

permute([1,2,3])