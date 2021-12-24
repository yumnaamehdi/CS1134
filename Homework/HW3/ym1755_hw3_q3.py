# Correcrt answer
def find_duplicates(lst):
    indexlst=[0]*(len(lst))
    outputlst=[]
    for i in range(len(lst)):
        if indexlst[lst[i]]!=-1:
            if indexlst[lst[i]]==lst[i]:
                indexlst[lst[i]]=-1
                outputlst.append(lst[i])
            elif indexlst[lst[i]]==0:
                indexlst[lst[i]]=lst[i]
    return outputlst
  
  #Wrong answer
  
def find_duplicates(lst):
    counts_of_all_ints = {}
    for i in lst:
        if i not in counts_of_all_ints:
            counts_of_all_ints[i] = 0
        else:
            counts_of_all_ints[i] += 1
    duplicates = [e for e in counts_of_all_ints if counts_of_all_ints[e] > 0]
    return duplicates
