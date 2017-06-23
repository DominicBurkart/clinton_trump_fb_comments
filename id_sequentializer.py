from pandas import *

import sys

is_tsv = True

try:
    if (sys.argv[1].lower().endswith("tsv")):
        data = read_table(sys.argv[1])
    elif (sys.argv[1].lower().endswith("csv")):
        is_tsv = False;
        data = read_csv(sys.argv[1])
    else:
        print("The input filetype could not be inferred by the file name. attempting to parse as TSV.")
        data = read_table(sys.argv[1])
except OSError:
    print("The given input does not point to a valid file. Please try again! Input: "+sys.argv[1])
    print("Quitting.")
    sys.exit()
except IndexError:
    print("No input was passed; quitting. Come back with data for me to eat!")
    sys.exit()
    
comm_ids = data.comment_id.tolist()
post_ids = data.post_id.tolist()
comm_ids_u = list(set(comm_ids))
post_ids_u = list(set(post_ids))
comm_seq = []
post_seq = []

cd = {}
pd = {}

for i in range(len(comm_ids_u)): #dicts are faster than getting indices
    cd[comm_ids_u[i]] = i
for i in range(len(post_ids_u)):
    pd[post_ids_u[i]] = i

i = 0
for x in comm_ids:
    comm_seq.append(cd[x])
    if (i % 1000 == 0):
        print(str(i/len(comm_ids)*100) + "% complete rewriting comment ids")
    i = i + 1
print("finished with comment ids.")
i = 0
for x in post_ids:
    post_seq.append(pd[x])
    if (i % 1000 == 0):
        print(str(i/len(comm_ids)*100) + "% complete rewriting post ids")
    i = i + 1
print("finished with post ids. writing out.")

data.comment_id = comm_seq
data.post_id = post_seq

if is_tsv:
    data.to_csv(sys.argv[1], index=False, sep="\t", doublequote=False, escapechar="\\")
else:
    data.to_csv(sys.argv[1], index=False, escapechar="\\")
print("resequentialization complete.")
