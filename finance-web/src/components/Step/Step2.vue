<template>
    <div class="container">
        <div class="head">
            <el-icon color="#909399" style="margin-right:12px;"><data-analysis /></el-icon>
            <span >数据分析</span>
            <span style="font-size:13px;color:#0984E3;margin-left:166px;margin-right:12px;">对数据进行预测:</span>
            <el-button type="primary" @click="predict">欺诈预测</el-button>
            <el-divider style="background-color: #7f8c8d;"></el-divider>
        </div>
        <div class="content">
            <div class="left">
                <div class="left-up">
                    <div id="chart1"></div>
                    <div class="title">工作年限(年)</div>
                </div>
                <div class="left-down">
                    <div id="chart2"></div>
                    <div class="title">贷款金额情况(元)</div>
                </div>
            </div>
            <div class="right">
                <div class="title">信誉等级分布</div>
                <div id="chart3"></div>
            </div>
        </div>
    </div>
</template>

<script>
import {DataAnalysis} from '@element-plus/icons-vue'
import * as echarts from 'echarts'
import axios from '../../req.js'
import { ElLoading } from 'element-plus'
import { Msg } from '../../utils/msg.js'

export default {
    data(){
        return {
            filename:""
        }
    },
    components:{
        DataAnalysis
    },
    mounted(){

        let filename = this.$route.params.filename
        if(filename == undefined){
            Msg("非法操作，请先点击下方 开始分析","error")
            this.$router.push("/step/step1")
            return
        }
        this.filename = filename
        const loading = ElLoading.service({
            lock: true,
            text: 'Loading',
            background: 'rgba(0, 0, 0, 0.7)',
        })

        let chart1 = echarts.init(document.getElementById("chart1"));
        let chart2 = echarts.init(document.getElementById("chart2"));
        let chart3 = echarts.init(document.getElementById("chart3"));

        let data1 = []
        let data2 = []
        let data3 = []

        // chart1 获取工作年限情况
        axios({
            method:'get',
            url:'/api/getEmpData',
            params:{
                filename:filename
            }
        }).then(res=>{
            console.log("res",res.data.info)
            data1 = res.data.info
            let option1 = this.chart1(data1);

            console.log(data1)

            chart1.setOption(option1);

            // chart2 获取贷款金额情况
            axios({
                method:'get',
                url:'/api/getLoanData',
                params:{
                    filename:filename
                }
            }).then(res=>{
                console.log("res",res.data.info)
                data2 = res.data.info
                let option2 = this.chart2(data2);
                chart2.setOption(option2);

                // chart3 获取贷款金额情况
                axios({
                    method:'get',
                    url:'/api/getGradeData',
                    params:{
                        filename:filename
                    }
                }).then(res=>{
                    console.log("res",res.data.info)
                    data3 = res.data.info
                    let option3 = this.chart3(data3);
                    chart3.setOption(option3);

                    loading.close()

                })

            })

        })

        
    },
    methods:{
        chart1(data){
            let option = {
                color:"#f6b93b",
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'shadow'
                    }
                },
                toolbox: {
                    show: true,
                    feature: {
                    mark: { show: true },
                    // dataView: { show: true, readOnly: false },
                    // restore: { show: true },
                    saveAsImage: { show: true }
                    }
                },
                xAxis: {
                    type: 'category',
                    data: ['<2', '<4', '<6', '<8', '>8']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        name:'工作年限',
                        data: data,
                        type: 'line'
                    }
                ]
            };
            return option
        },
        chart2(data){
            let option = {
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                        type: 'shadow'
                        }
                    },
                    toolbox: {
                        show: true,
                        feature: {
                        mark: { show: true },
                        // dataView: { show: true, readOnly: false },
                        // restore: { show: true },
                        saveAsImage: { show: true }
                        }
                    },
                    color:'#0984e3',
                    xAxis: {
                        type: 'category',
                        data: ['<5000', '<10000', '<15000', '<20000', '<25000','<30000','>30000']
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                        name:'贷款金额情况',
                        data: data,
                        type: 'bar',
                        barWidth:26,
                        showBackground: true,
                        backgroundStyle: {
                            color: 'rgba(180, 180, 180, 0.2)'
                        }
                        }
                    ]
            };
            return option
        },
        chart3(data){
            let option = {
                legend: {
                    top: 'bottom'
                },
                  tooltip: {
                    trigger: 'item'
                },
                toolbox: {
                    show: true,
                    feature: {
                    mark: { show: true },
                    // dataView: { show: true, readOnly: false },
                    // restore: { show: true },
                    saveAsImage: { show: true }
                    }
                },
                series: [
                    {
                    name: '信誉等级分布',
                    type: 'pie',
                    radius: [50, 180],
                    center: ['50%', '50%'],
                    roseType: 'area',
                    itemStyle: {
                        borderRadius: 8
                    },
                    data:data
                    }
                ]
            };
            return option
        },
        predict(){
            this.$router.push("/step/step3/"+this.filename)
        }
    }
}
</script>

<style scoped>
.container{
    margin:16px 60px;
    display: flex;
    flex-direction: column;
    height: 660px;
    font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB',
  'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
}
.container .head{
    flex:1;
    font-size: 21px;
    width: 100%;
    text-align: center;
    margin-top: 30px;
    
}
.container .content{
    flex:9;
    display: flex;
}

.content .left{
    flex:1;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
}

.content .left .left-up{
    flex:1;
    height: 46%;
}

.content .left .left-up #chart1{
    width:100%;
    height: 95%;
}

.content .left .left-down{
    flex:1;
    height: 46%;
}

.content .left .left-down #chart2{
    width:100%;
    height:93%;
}

.content .right{
    flex:1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.content .right #chart3{
    height: 88%;
    width:96%;
}

.content .right .title,.left-down .title,.left-up .title{
    text-align: center;
}

</style>
