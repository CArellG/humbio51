data=open("E116_15_coreMarks_dense.bed",'r').read().strip().split('\n')
import random
subset=random.sample(data,10000)
import numpy as np

#Add Gaussian noise
noise=np.random.normal(0,0.02,(10000,5))

state_map=open("state_map.txt",'r').read().strip().split('\n')
state_dict=dict()
for line in state_map:
    tokens=line.split('\t')
    state_dict[tokens[0]]='\t'.join(tokens[1::])
print(str(state_dict))
outf=open("region_x_chrom_mark.tsv",'w')
outf.write("chrom_start_end\tH3K4me3\tH3K4me1\tH3K36me3\tH3K9me3\tH3K27me3\n")
outf2=open("region_x_annotation.tsv",'w')
outf2.write("chrom_start_end\tAnnotation\n")

counter=0 
for entry in subset:
    tokens=entry.split('\t')
    chrom=tokens[0]
    start=tokens[1]
    end=tokens[2]
    state=state_dict[tokens[3]].split('\t')
    state=[float(i) for i in state]
    cur_noise=list(noise[counter])
    noisy=[state[i]+cur_noise[i] for i in range(len(cur_noise))]
    noisy=[str(i) for i in noisy]
    noisy='\t'.join(noisy)
    outf.write(chrom+"_"+start+"_"+end+"\t"+noisy+"\n")
    outf2.write(chrom+"_"+start+"_"+end+"\t"+tokens[3]+"\n")
    counter+=1 

