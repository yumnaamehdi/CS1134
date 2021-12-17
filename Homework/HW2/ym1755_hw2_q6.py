
def two_sum(srt_lst, target):
    for i in range(len(srt_lst)):
        if (target - srt_lst[i]) in srt_lst:
            return (i, srt_lst.index(target-srt_lst[i]))
