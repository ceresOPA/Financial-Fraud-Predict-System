# 金融反欺诈预测系统（Financial-Fraud-Predict-System）

[![](https://img.shields.io/badge/github-%E4%B8%8D%E6%83%B3%E5%BD%93%E5%BA%9F%E7%89%A9%E7%9A%84%E7%82%AE%E7%81%B0%E9%B1%BC-brightgreen)](https://github.com/ceresOPA)  [![](https://img.shields.io/badge/bilibili-%E6%98%AF%E4%B9%90%E9%81%93%E9%95%BF-9cf)](https://space.bilibili.com/510005777) [![](https://img.shields.io/badge/License-MIT-orange)](./LICENSE) <br/>


金融反欺诈预测系统，本人本科期间项目，技术涉及Vue3、Flask、XGBoost等。本项目提供了完整的Web系统，系统功能包括信贷数据分析、信贷欺诈数据检测、用户历史预测记录、用户数据管理等。项目整体并不复杂，适合新手练手学习机器学习与Web系统的结合。

本项目代码分为三部分：数据分析与模型构建、Web前端系统、服务端。(如果想直接使用本系统的同学可以忽略数据分析与模型构建部分，直接按照说明完成项目的部署)

## 环境配置

Python依赖库（推荐使用**anaconda**等虚拟环境，同时配置镜像源）

```shell
pip install -r requirement.txt
```

node.js依赖模块（node推荐使用V16.13.1版本，该版本为本项目实际使用环境，node有时候会出现兼容性问题）

```shell
cd finace-web
npm install
```

## 数据分析与模型构建

进入finace-analysis目录，打开notebook

```shell
cd finace-analysis
jupyter notebook
```

具体分析过程可以自行查看，数据集来源为美国P2P平台提供的LoanStats数据，网上均有分享

## 项目部署

本项目为前后端分离式的系统，只要完成环境的配置后，分别部署前端和后端即可。

### Finace-server

服务端采用Flask框架，为前端提供的API位于route文件下

```shell
cd ./finace-server
python main.py
```

### Finace-web

前端采用Vue3实现，使用UI框架为element-plus 

```shell
cd ./finace-web
npm run dev
```

## 相关技术