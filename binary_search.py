def bin_Search(sorted_arr,item):
    start=0
    end=len(sorted_arr)-1
    pos=end//2
    while(sorted_arr[pos]!=item):
        if (sorted_arr[pos]>item):
            end=pos
            pos=end//2
        else:
            start=pos
            pos=start//2
