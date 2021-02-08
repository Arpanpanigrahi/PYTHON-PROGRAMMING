from collections import Counter
votes=['arpan','ashish','aditya','arpan','aditya','arpan','arpan']
votecount=Counter(votes)
maximum_votes=max(votecount.values())
1st = [i for i in votecount.keys()) if votecount[i]==maximum_votes]
print(sorted(1st)[0])
