"""

Chunking problem:

remove duplicates from a given huge array by using merge - sort style
Algorithm:

Chunk a given string S so that the chunks can fit ito memory 
Sort individual chunks and remove duplicates
and merge them iteratively

This algorithm will have O(2*N) disk swaps where N is the number of chunks 
Time complexity : N*O(MlogM)*logN , where M is the chunk size
MlogM -> for individual chunk sorts , logN  for  number of iterations on while loop  and N  cuz N_chunks 

"""

def driver():

    s1 = ['1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3']
    n_chunks = 5
    chunk_size = len(s1)/n_chunks + 1

    
    while True:

        res = []
        for i in  xrange(n_chunks):

            chunk = s1[i*chunk_size:(i+1)*chunk_size]
            chunk.sort()
            #import pdb; pdb.set_trace()
            res.extend(list(set(chunk)))
        
        s1 = res
        n_chunks /= 2
        if n_chunks == 0:
            break

        chunk_size = len(s1)/n_chunks + 1
    
    print s1

driver()

