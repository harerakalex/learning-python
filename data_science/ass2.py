import pandas as pd
import numpy as np

df = pd.read_csv('readonly/NISPUF17.csv', index_col=0)

cols = df.columns
len(cols)

def proportion_of_education():
    edus = np.sort(df['EDUC1'].values)
    
    poe = {"less than high school": 0,
        "high school": 0,
        "more than high school but not college": 0,
        "college": 0}
    n = len(edus)
    
    poe["less than high school"] = np.sum(edus == 1)/n
    poe["high school"] = np.sum(edus == 2)/n
    poe["more than high school but not college"] = np.sum(edus == 3)/n
    poe["college"] = np.sum(edus == 4)/n
    
    return poe
proportion_of_education()

def average_influenza_doses():
    cbf_flu=df.loc[:,['CBF_01','P_NUMFLU']]
    
    
    cbf_flu1=cbf_flu[cbf_flu['CBF_01'] ==1].dropna()
    cbf_flu2=cbf_flu[cbf_flu['CBF_01'] ==2].dropna()
    
    flu1=cbf_flu1['P_NUMFLU'].values.copy()
    flu1[np.isnan(flu1)] = 0
    f1=np.sum(flu1)/len(flu1)
    
    flu2=cbf_flu2['P_NUMFLU'].values.copy()
    flu2[np.isnan(flu2)] = 0
    f2=np.sum(flu2)/len(flu2)
    
    aid =(f1,f2)
    return aid
average_influenza_doses()

def chickenpox_by_sex():
    cpo_sex=df[df['P_NUMVRC'].gt(0) & df['HAD_CPOX'].lt(3)].loc[:,['HAD_CPOX','SEX']]
    #Male 1 Female 2
    cpo1_sex1=len(cpo_sex[(cpo_sex['HAD_CPOX']==1) & (cpo_sex['SEX']==1)])
    cpo1_sex2=len(cpo_sex[(cpo_sex['HAD_CPOX']==1) & (cpo_sex['SEX']==2)])
    cpo2_sex1=len(cpo_sex[(cpo_sex['HAD_CPOX']==2) & (cpo_sex['SEX']==1)])
    cpo2_sex2=len(cpo_sex[(cpo_sex['HAD_CPOX']==2) & (cpo_sex['SEX']==2)])
    
    cbs={"male":0,
        "female":0}
    cbs['male']=cpo1_sex1/cpo2_sex1
    cbs['female']=cpo1_sex2/cpo2_sex2
    return cbs
chickenpox_by_sex()

def corr_chickenpox():
    import scipy.stats as stats
    import pandas as pd
    import numpy as np

    df = pd.read_csv('readonly/NISPUF17.csv', index_col=0)
    
    df=df[df['HAD_CPOX'].lt(3)].loc[:,['HAD_CPOX','P_NUMVRC']].dropna()
    df.columns=['had_chickenpox_column','num_chickenpox_vaccine_column']
    # here is some stub code to actually run the correlation
    corr, pval=stats.pearsonr(df["had_chickenpox_column"],df["num_chickenpox_vaccine_column"])
    
    # just return the correlation
    return corr
corr_chickenpox()