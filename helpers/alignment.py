import subprocess
def align(sample,reference,outputf):
    command_args=["bowtie2","-x",reference,"-f","-U",sample,"-S",outputf]
    proc = subprocess.Popen (command_args, shell=False, stdout=subprocess.PIPE)
    out = proc.communicate()[0]
    #print the output of the child process to stdout
    print (out)


def select_column(outputf,column):
    data=open(outputf,'r').read().strip().split('\n')
    tokens=[line.split('\t')[column] for line in data[3::]]
    print('\n'.join(tokens))
