#helper scripts
def load_rnaseq_data(systems_subset="all",
                     filepath='../datasets/RNAseq/diff_genes_top_1000.tsv',
                     batches='../datasets/RNAseq/rnaseq_batches.txt'):
    import pandas as pd
    data=pd.read_csv(
        filepath_or_buffer=filepath,
        header=0,
        sep='\t')
    batches= pd.read_csv(
             filepath_or_buffer=batches,
             header=0,
             sep='\t')
    if systems_subset=="all":
        return data,batches
    else: 
        batches_subset=batches.loc[batches['System'].isin(systems_subset)]
        data_subset=data.loc[:,batches_subset['Sample']]
        batches_subset=batches_subset.reset_index()
        return data_subset,batches_subset

    

