<template>
    <div class="container">
        <div class="introduce">
            <div class="head_title">
                <el-icon color="#909399" style="margin-right:6px;"><info-filled /></el-icon>
                <span>字段详情：</span>
                <span style="font-size:12px;">(点击可展开查看详情)</span>
            </div>
            <div class="info">
                  <div class="demo-collapse">
                    <el-collapse >
                        <el-collapse-item v-for="item,index in filedList" :key="index" :title="item.title" >
                            <div>
                                {{item.info}}
                            </div>
                        </el-collapse-item>
                    </el-collapse>
                </div>
            </div>
        </div>
        <div class="upload_file">
                <el-upload
                class="upload_block"
                accept=".csv,.xls,.xlsx"
                drag
                action="/api/upload"
                :on-success="fileRespone"
                :limit="1"
                :file-list="fileList"
            >
                <el-icon class="el-icon--upload"><upload-filled /></el-icon>
                <div class="el-upload__text">
                    将文件拖至框内或<em>点击进行上传</em>
                </div>
                <template #tip>
                    <div class="el-upload__tip">
                        仅限csv、xls、xlsx文件
                    </div>
                </template>
            </el-upload>
        </div>
        <div class="analysis">
            <el-button type="primary" @click="analyze">点击开始分析</el-button>
        </div>
    </div>
</template>


<script>
import {InfoFilled ,UploadFilled} from '@element-plus/icons-vue'
import {Msg} from '../../utils/msg.js'
import axios from '../../req.js'

    export default {
        name:'Step1',
        components:{
            InfoFilled,
            UploadFilled
        },
        data(){ 
            return {
                filedList:[
                    {
                        title:"loan_amnt(贷款金额)",
                        info:"用户贷款金额"
                    },
                    {
                        title:"term(贷款期限)",
                        info:"贷款期限，单位为月"
                    },
                    {
                        title:"int_rate(贷款利率)",
                        info:"贷款利率，单位为百分率"
                    },
                    {
                        title:"grade(信誉等级)",
                        info:"信誉等级可分为A-G，表示由高到低，用户也可直接用数值表示，数值越大信誉越高"
                    },
                    {
                        title:"home_ownership(住房情况)",
                        info:"住房情况：RENT:租房；MORTGAGE:抵押；OWN:拥有"
                    },
                    {
                        title:"emp_length(工作年限)",
                        info:"整型；如1、2、3、10"
                    }
                    
                ],
                file:{},
                fileList:[]
            }
        },
        mounted(){
            if(localStorage.file!=undefined&&localStorage.file!=null){
                let file = JSON.parse(localStorage.file)
                if(file!=null&&file!=undefined){
                    this.fileList.push({
                        name:file.filename.split("_")[1],
                        url:file.file_url
                    })
                    this.file = file
                }
            }
 
        },
        methods:{
            fileRespone(res, file, fileList){
                // console.log(res,file,fileList)
                if(res.state == 'success'){
                    Msg("上传成功","success")
                    this.file = {
                        filename : res.info.filename,
                        file_url : '/uploads/'+res.info.filename
                    }
                    localStorage.setItem("file",JSON.stringify(this.file))
                }else{
                    Msg(res.msg,'error')
                }
                
            },
            analyze(){
                this.$router.push('/step/step2/'+this.file.filename)
            }
        }
    }
</script>

<style scoped>
.container{
    margin:66px 160px;
    display: flex;
    flex-direction: column;
    height: 620px;
    font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB',
  'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
}
.container .introduce{
    flex: 5;
}

.container .introduce .head_title{
    font-size: 21px;
}

.container .upload_file{
    flex:2;
    display: flex;
    justify-content: center;
    align-content: center;
}

.container .analysis{
    margin-top: 20px;
    display: flex;
    justify-content: center;
    align-content: center;
    flex:1;
}

</style>
