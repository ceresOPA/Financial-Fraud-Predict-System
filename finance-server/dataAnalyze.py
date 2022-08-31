import pandas as pd

def getFile(filename):
    extense = filename.split('.')[1]
    if(extense == 'csv'):
        file = pd.read_csv(f"./uploads/{filename}")
    elif(extense == 'xls' or extense == 'xlsx'):
        file = pd.read_excel(f"../uploads/{filename}")
    if("Unnamed: 0" in file.columns):
        file.drop("Unnamed: 0",axis=1,inplace=True)
    return file
    
def getLoanAmount(filename):
    file = getFile(filename)
    data = []
    #小于3000的数量
    data.append(file[file['loan_amnt']<5000].shape[0]) 
    data.append(file[file['loan_amnt']<10000].shape[0] - file[file['loan_amnt']<5000].shape[0])
    data.append(file[file['loan_amnt']<15000].shape[0] - file[file['loan_amnt']<10000].shape[0])
    data.append(file[file['loan_amnt']<20000].shape[0] - file[file['loan_amnt']<15000].shape[0])
    data.append(file[file['loan_amnt']<25000].shape[0] - file[file['loan_amnt']<20000].shape[0])
    data.append(file[file['loan_amnt']<30000].shape[0] - file[file['loan_amnt']<25000].shape[0])
    data.append(file[file['loan_amnt']>30000].shape[0])
    return data

def getEmpAmount(filename):
    file = getFile(filename)
    data = []
    data.append(file[file['emp_length']<2].shape[0]) 
    data.append(file[file['emp_length']<4].shape[0] - file[file['emp_length']<2].shape[0])
    data.append(file[file['emp_length']<6].shape[0] - file[file['emp_length']<4].shape[0])
    data.append(file[file['emp_length']<8].shape[0] - file[file['emp_length']<6].shape[0])
    data.append(file[file['emp_length']>8].shape[0])
    return data

from predict import preprocessing

def getGradeAmount(filename):
    file = getFile(filename)
    file = preprocessing(file)
    data = []
    for i in range(7):
        item = {}
        item['value'] = file[file['grade']==(7-i)].shape[0]
        item['name'] = '等级'+chr(65+i)
        data.append(item)
    return data

def getAmount(filename):
    file = getFile(filename)
    size = file.shape
    return {
        'row':size[0],
        'column':size[1]
    }