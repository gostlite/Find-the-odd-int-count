# get highest count
def find_it(seq):
    the_c = 0
    counts = [seq.count(i) for i in seq]
    for count in counts:
        
        if count%2 != 0:
            for i in range(len(counts)):
                if seq.count(seq[i]) == count:
                   the_cc = seq[i]
                   the_c = the_cc
    return the_c
            # for i in seq:





a = [2,2,2,3,4,3,5,4,2]
c = find_it(a)
print(c)
