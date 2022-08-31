import pandas as pd
from dataAnalyze import getFile
import joblib
from sklearn.preprocessing import StandardScaler

# ------------------- 预处理阶段 ---------------------

def Grade2Value(x):
    if(ord(x)>=65):
        return ord('H')-ord(x)
    return x.astype(int)

def Home2Value(x):
    if(x=='MORTGAGE'):
        return 1
    elif(x=='RENT'):
        return 2
    elif(x=='OWN'):
        return 3

def preprocessing(file):
    # 深拷贝一份，不改变原数据
    df = file.copy(deep=True)
    # 利率类型转float
    df['int_rate'] = df['int_rate'].astype(str).str[:-1].astype(float)
    # 信誉等级转数值类型
    df['grade'] = df.grade.apply(lambda x:Grade2Value(x))
    # 住房情况转换为数值类型
    df['home_ownership'] =df.home_ownership.apply(lambda x:Home2Value(x))
    # 检查每个字段的数据类型是否已全部转换为数值类型
    # for i in range(df.shape[1]):
    #     if(df.dtypes[i]=='object'):
    #         return {}
    # 归一化处理,z-score 标准正态分布
    # std = StandardScaler()
    # std_x = std.fit_transform(df)
    return df


# ------------------- 预处理阶段 ---------------------

def predictLabel(file):
    # 预处理,获取合法样本
    x = preprocessing(file)
    # if(x=="error"):
    #     return "error"
    # 加载模型
    xgb = joblib.load("./model/xgb_plus.joblib")
    y_pred = xgb.predict(x)

    return y_pred


def getPredictData(filename):
    # DataFrame格式数据
    file = getFile(filename)
    # 获取预测的label
    label_pred = predictLabel(file)
    # if(label_pred=="error"):
    #     return {
    #         'state':'fail',
    #         'msg':'数据格式存在错误'
    #     }
    print("--------------------",label_pred)
    file['tag'] = label_pred
    file.to_csv(f"./uploads/res_{filename}")
    return_file = file.iloc[:500,:]
    # DataFrame转换为json数据
    json_data = return_file.to_json(orient='records',force_ascii=False)
    return {
        'state':'success',
        'info':json_data,
        'res_url':f"/uploads/res_{filename}"
    }