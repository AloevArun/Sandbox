S = str(input())
# S = "dgdhhhhdgggdss"

strlen = len(S)
i, j = 0, 1
while j != strlen:
    itersymb = S[i]
    kpb = 1
    while S[i] == S[j]:
        kpb += 1
        i += 1
        j += 1
    i += 1
    j += 1
    print((itersymb + str(kpb)), end='')
print((itersymb + str(kpb)), end='')
