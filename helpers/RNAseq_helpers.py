#helper scripts
def load_rnaseq_data(systems_subset="all",
                     filepath
                     batches)
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
        data=data[batches.sort_values(by="System")["Sample"]]
        #data.columns=batches.sort_values(by="System")["System"]
        return data,batches
    else: 
        batches_subset=batches.loc[batches['System'].isin(systems_subset)]
        data_subset=data.loc[:,batches_subset['Sample']]
        batches_subset=batches_subset.reset_index()
        data_subset=data_subset[batches_subset.sort_values(by="System")["Sample"]]
        #data_subset.columns=batches_subset.sort_values(by="System")["System"]
        return data_subset,batches_subset

    

