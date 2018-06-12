import pandas as pd
import os, shutil


SNF = pd.read_csv('SNFcsv.csv')
acceptedSNF = SNF[SNF['Status'] == 'Approved']['SNF_ID']

accepted = SNF[SNF['Status'] == 'Approved']
accepted['SNF_ID'].astype('int')



os.chdir(r'C:\Users\RFiedler\PycharmProjects\quickbase\ApprovedSNFs')
files = [f for f in os.listdir(r'C:\Users\RFiedler\PycharmProjects\quickbase\ApprovedSNFs') if os.path.isfile(f)]


for file in files:
    filename = file.split('.')[0]
    SNFnumber = filename.split('_')[1]
    SNFnumber = int(SNFnumber)
    #print(SNFnumber)
    partnumber = accepted[accepted['SNF_ID'] == SNFnumber]['Part_Number'].astype('str')
    partnumber.values[0]
    newname = partnumber + '_' + file
    os.rename(file, str(newname.values[0]))




