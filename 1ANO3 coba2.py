ulang = int(input())
for u in range (1,ulang+1):
    word = {}
    N = int(input())
    for i in range (0,N):
        temp = input()
        for j in range (0,len(temp)):

            if temp[j:] in word:
                word[temp[j:]] += 1
            else:
                word[temp[j:]]=1
    
   
    doneKey= []
    ryhme = 0
    ListOfKeys = []
    alreadyIn = False

    for k in word:
        ListOfKeys.append(k)
    ListOfKeys.sort(key = lambda s:len(s),reverse=True)
    
    
    for i in ListOfKeys:
       
        if word[i] > 1:
            for j in range (0,len(doneKey)):
                
                if i == doneKey[j]:
                    alreadyIn = True
                    break
            
            if alreadyIn== True :
                continue
            else:
                
                for l in word:
                    if l in i:
                        word[l] -= 2
                ryhme += 2
                doneKey.append(i)
                if ryhme == N:
                    break
    
    
    print ("Case #{}: {}".format(u,ryhme))
