#helper scripts
def load_rnaseq_data(systems_subset,
                     filepath,
                     batches):
    import pandas as pd
    data=pd.read_csv(
        filepath_or_buffer=filepath,
        header=0,
        index_col=0,
        sep='\t').transpose()
    batches= pd.read_csv(
             filepath_or_buffer=batches,
             header=0,
             index_col=0,
             sep='\t')
    nrow_data,ncol_data=data.shape
    nrow_batches,ncol_batches=data.shape 
    merged_df=pd.merge(data, batches, left_index=True,right_index=True)
    if systems_subset=="all":
        data_filtered=merged_df.iloc[:,0:ncol_data].transpose()
        batches_filtered=merged_df.iloc[:,0:-1*ncol_batches]
    else:
        samples_to_keep=merged_df['System'].isin(systems_subset)
        merged_df_subset=merged_df[samples_to_keep]
        data_filtered=merged_df_subset.iloc[:,0:ncol_data].transpose()
        batches_filtered=merged_df_subset.iloc[:,0:-1*ncol_batches]
    return data_filtered,batches_filtered

