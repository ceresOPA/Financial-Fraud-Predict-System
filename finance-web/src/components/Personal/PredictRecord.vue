<template>
    <div class="container">
        <h1 style="margin-bottom:26px;">检测记录</h1>
        <p style="margin:6px;font-size:12px;color:#2D2D2D;">仅保留最近10条记录</p>
        <el-table :data="tableData" height="600" style="width: 80%">
        <el-table-column prop="account" label="账号" width="120" />
        <el-table-column prop="date" label="检测时间" width="200" />
        <el-table-column prop="file_url" label="检测文件" width="360" />
        <el-table-column fixed="right" type="index" label="下载检测结果" width="150">
        <template #default="scope">
            <el-button type="text" size="small" 
            ><el-icon><download /></el-icon><a :href="'./api/uploads/'+scope.row.file_url">下载</a></el-button>
             <el-button type="text" size="small" style="color:#FF8F6B;" @click="delete_record(scope.row.id)" 
            ><el-icon><delete /></el-icon>删除</el-button>
        </template>
        </el-table-column>
        </el-table>
    </div>
</template>

<script>
import { Download,Delete } from '@element-plus/icons-vue'
import axios from '../../req.js'

import { Msg } from '../../utils/msg.js'
import { ElMessage, ElMessageBox } from 'element-plus'

import { ElLoading } from 'element-plus'

    export default {
        data(){
            return {
                tableData:[
                    {
                        account:"yule",
                        date: '2022-01-16 11:12:32',
                        file_url: '131231313_test.csv'
                    },
                      {
                        account:"yule",
                        date: '2022-01-16 11:26:32',
                        file_url: '132391313_train.csv'
                    },
                     {
                        account:"yule",
                        date: '2022-01-15 16:26:32',
                        file_url: '132391313_raw_test.xls'
                    }
                ]
            }
        },
        mounted(){

            let user = JSON.parse(localStorage.user)
            let that = this

            const loading = ElLoading.service({
                lock: true,
                text: 'Loading',
                background: 'rgba(0, 0, 0, 0.7)',
            })

            axios({
                method:'post',
                url:'./api/getrecord',
                data:{
                    account:user.account
                }
            }).then((res)=>{
                console.log(res.data)
                that.tableData = res.data.record
                loading.close()
            })
            
        },
        methods:{

            delete_record(record_id){

                let user = JSON.parse(localStorage.user)
                let that = this

                ElMessageBox.confirm(
                '确定删除该条记录？',
                '提醒',
                {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'warning',
                }).then(()=>{
                    axios({
                        method:'post',
                        url:'./api/deleterecord',
                        data:{
                            id:record_id,
                            account:user.account
                        }
                    }).then((res)=>{
                        console.log(res.data)
                        if(res.data.state == 'success'){
                            Msg("删除成功","success")
                        }else{
                            Msg("发生错误","error")
                        }
                        that.tableData = res.data.record
                    })
                })
                

                // axios({

                // })
            }

        },
        components:{
            Download,
            Delete
        }
    }
</script>

<style scoped>

a{
    text-decoration: none;
    color: #60AFFF;
}

.container{
    margin-left: 36px;
    display: flex;
    flex-direction: column;
}

</style>