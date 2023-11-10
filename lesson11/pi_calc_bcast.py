#combinbing pi calc solution from lesson 1 to gather and bcast in lesson 11
#import MPI
from mpi4py import MPI

#get the communicator
comm = MPI.COMM_WORLD

#get the rank
rank = comm.rank


#from parallel_generate_frames
# get the total number of processes
total_ranks = comm.size #number of copies running

#set the amount of work (number of terms)
total_work = 10000
#get the amount of work per worker
work_per_worker = total_work / total_ranks

#Define number of frames based on number of workers
start_ind = int(rank * work_per_worker)
end_ind = int((rank + 1)* work_per_worker -1)

#define the number of frames based on the numbr of workers (ranks)
#i = my_rank
for i in range(start_ind, end_ind + 1):

# set theindividual result for each rank
my_number = rank

#gather the results on rank 0
full_list = comm.gather(my_number, root = 0)
##pi_terms used to be my_number


# initialize pi to 0
pi = 0

# set the number of terms in the sum
N = 10000

# initialize an empty list store each term, so we can plot convergence later
pi_terms = []

# loop from 1 to N, adding terms to pi
# such that pi ~= 4*(1 - 1/3 + 1/5 - 1/7 + 1/9 ... -(-1)**n / (2n - 1))
for n in range(1,N):
    if n == 1:
        term = 1
    else:
        term = -((-1)**n) / (2*n - 1)
    pi = pi + term
    
    # store the term
    pi_terms.append(4*pi)

# multiply pi by four to get the final answer
pi = 4 * pi


#calculate avg rank; only 0 can do this
if rank ==0:
    new_pi = sum(pi) / len(pi)
else: 
    new_pi = None

# print the answer
print(f"pi = {new_pi}")