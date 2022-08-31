<template>
  <div class="container">
      <div class="head">
            <el-icon style="color:orange;font-size:26px;"><orange /></el-icon>
            <span style="font-size:21px;margin-right:36px;">数据欺诈预测</span>
            <el-button type="primary" @click="return_predict">重新预测</el-button>
      </div>
      <div class="line"></div>
      <div class="content">
          <div class="result-table">
            <el-button @click="clearFilter">重置筛选</el-button>
            <el-table ref="tableRef"  :data="tableData" height="526" style="width: 100%">
                <el-table-column prop="loan_amnt" label="loan_amnt" width="188" />
                <el-table-column prop="term" label="term" width="188" />
                <el-table-column prop="int_rate" label="int_rate" width="188" />
                <el-table-column prop="grade" label="grade" width="188" />
                <el-table-column prop="home_ownership" label="home_ownership" width="188" />
                <el-table-column prop="emp_length" label="emp_length(months)" width="188" />
                <el-table-column
                prop="tag"
                label="Tag"
                width="188"
                :filters="[
                    { text: '正常', value: 0 },
                    { text: '异常', value: 1 },
                ]"
                :filter-method="filterTag"
                filter-placement="bottom-end"
                >
                <template #default="scope">
                    <el-tag
                    :type="scope.row.tag === 1 ? 'danger' : 'success'"
                    disable-transitions
                    >{{ tag_name[scope.row.tag] }}</el-tag
                    >
                </template>
                </el-table-column>
            </el-table>
        </div>
        <div class="page">
            <span style="margin-left:126px;color:#909399;font-size:15px;">仅展示前500条数据，若需完整数据请<span style="color:#6B9EFF;cursor:pointer" @click="downloadRes"><a :href="res_url">点击下载</a></span></span>
            <el-pagination background layout="prev, pager, next"  :total="totalPages" v-model:current-page="currentPage" :page-size="20"  ></el-pagination>
        </div>
      </div>
  </div>
</template>

<script>
import { Orange } from '@element-plus/icons-vue'
import  axios from '../../req.js'
import { Msg } from '../../utils/msg.js'

import { ElLoading } from 'element-plus'

    export default {
        data(){
            return {
                tag_name:["正常","异常"],
                // tableData:[],
                totalPages:1,
                totalData:[],
                rawData:[],
                currentPage:1,
                isFilter:false,
                res_url:""
            }
        },
        mounted(){
            let filename = this.$route.params.filename
            let that = this
            if(filename == undefined){
                Msg("非法操作，请先上传文件","error")
                this.$router.push("/step/step1")
                return
            }

            const loading = ElLoading.service({
                lock: true,
                text: 'Loading',
                background: 'rgba(0, 0, 0, 0.7)',
            })
            let user = JSON.parse(localStorage.user)
            axios({
                method:'get',
                url:'/api/getPredictRes',
                params:{
                    filename,
                    account:user.account
                }
            }).then(res=>{
                let data = JSON.parse(res.data.info)
                console.log("data",data)
                console.log("data length",data.length)
                that.totalData = data
                that.totalPages = data.length
                that.res_url = res.data.res_url

                loading.close()
                // that.tableData = data.slice(0,20)
            })
        },
        components:{
            Orange
        },
        computed:{
            tableData(){
                let page_index = this.currentPage
                let data = this.totalData.slice((page_index-1)*20,page_index*20)
                return data
            }
        },
        methods:{
            filterTag(value,row){
                // console.log(value,row)

                if(!this.isFilter){
                    this.isFilter = true
                    this.rawData = this.totalData
                }else{
                    this.totalData = this.rawData
                }

                this.totalData = this.totalData.filter((x)=>x.tag==value)

                this.totalPages = this.totalData.length
                this.currentPage = 1

                return true
            },
            clearFilter(){
                this.currentPage = 1
                this.totalData = this.rawData
                this.totalPages = this.rawData.length
                // this.tableData = this.totalData.slice((page_index-1)*20,page_index*20)
                this.isFilter = false
                this.$refs.tableRef.clearFilter()
            },
            downloadRes(){
                Msg("下载成功","success")
            },
            return_predict(){
                this.$router.push('/step/step1')
            }
        }
    }
</script>

<style scoped>
.container{
    margin:30px 60px 10px 60px;
    display: flex;
    flex-direction: column;
    height: 660px;
    font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB',
  'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
}

.container .head{
    margin-bottom:30px;
    width:600px;
    display: flex;
    justify-content: flex-start;
}

.container .head .tag{

    width: 160px;
    height: 50px;
    font-size: 16px;
}

.result-table{
    margin-left: 120px;
}

.page{
    display: flex;
    justify-content: space-between;
    margin-right: 120px;
}

</style>