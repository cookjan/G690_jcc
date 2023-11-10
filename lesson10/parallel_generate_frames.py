from mpi4py import MPI
import generate_frame

#initialize MPI v 
# get the 'communicator'
comm = MPI.COMM_WORLD

# get the 'rank' of the process
my_rank = comm.rank #THIS DIFFERS BETWEEN COPIES OF THE PROGRAM its a communicator

# get the total number of processes
total_ranks = comm.size #number of copies running


#set the amount of work
total_work = 720
#get the amount of work per worker
work_per_worker = total_work / total_ranks

#Define number of frames based on number of workers
start_ind = int(my_rank * work_per_worker)
end_ind = int((my_rank + 1)* work_per_worker -1)



#define the number of frames based on the numbr of workers (ranks)
#i = my_rank
for i in range(start_ind, end_ind + 1):
    print(f"rank {my_rank}/{total_ranks}: {start_ind}/{end_ind} running")
    generate_frame.generate_frame(i)