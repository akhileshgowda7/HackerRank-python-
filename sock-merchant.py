def sockMerchant(n, ar):
    # Write your code here
    hashmap = {}
    
    for i in range(n):
        if ar[i] not in hashmap.keys():
            hashmap[ar[i]]=1
        else:
            hashmap[ar[i]]+=1
    count = 0      
    print(hashmap)
    for key in hashmap:
        if hashmap[key]%2==0:
            count+=hashmap[key]//2
        elif hashmap[key]>2:
            count+= (hashmap[key]-1)//2
    return count