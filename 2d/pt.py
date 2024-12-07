import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
#outdir='Results/000038'
#eigen_pratiofile=outdir + '/' + 'eigen_pratio.csv'
epfile_log = 'pratio_eigen.png'
eigenvalues_list=[]
pratio_list=[]
columns = defaultdict(list) # each value in each column is appended to a list
#folder=['000039','000033','000034','000035','000036']
folder=['000056']
for i in range(len(folder)):
    outdir='Results/'+folder[i]
    eigen_pratiofile=outdir + '/' + 'eigen_pratio.csv'
    with open(eigen_pratiofile) as f:
       fieldnames = ['eigenvalue','participation_ratio']
       reader = csv.DictReader(f) # read rows into a dictionary format
       for row in reader: # read a row as {column1: value1, column2: value2,...}
           for (k,v) in row.items(): # go over each column name and value 
              columns[k].append(np.float128(v)) # append the value into the appropriate list

eigenvalues_list+=np.array(columns['eigenvalue']).tolist()
pratio_list+=np.array(columns['participation_ratio']).tolist()

plt.clf()
plt.yscale('log')
#plt.ylim(0.001,1)
plt.scatter(eigenvalues_list,pratio_list,s=0.1)
plt.xlabel('eigenvalues')
plt.ylabel('p-ratio')
plt.savefig(epfile_log)
print("> pratio vs eigenvalues to {}".format(epfile_log))

