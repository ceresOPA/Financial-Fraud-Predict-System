<template>
    <div class="step">
        <div @click="step(0)" class="step1" :style="{backgroundColor:stepBgColor[0]}"><div style="transform:skewX(45deg)"><router-link to="/step/step1">Step1：数据上传</router-link></div></div>
        <div @click="step(1)" class="step2" :style="{backgroundColor:stepBgColor[1]}"><div style="transform:skewX(45deg)"><router-link to="/step/step2">Step2：数据分析</router-link></div></div>
        <div @click="step(2)" class="step3" :style="{backgroundColor:stepBgColor[2]}"><div style="transform:skewX(45deg)"><router-link to="/step/step3">Step3：模型预测</router-link></div></div>
    </div>
    <div class="content">
        <router-view></router-view>
    </div>
</template>

<script>

    import { changeStepColor } from "../../utils/tools.js"
    export default {
        data(){
            return {
                stepBgColor:[
                    "#7ed6df",
                    "#7ed6df",
                    "#7ed6df"
                ]
            }
        },
        mounted(){
            setInterval(() => {
                changeStepColor(this)
            }, 500);
        },
        methods:{
            step(x){
                switch(x){
                    case 0:
                        this.stepBgColor = ["#7ed6df","#7ed6df","#7ed6df"]
                        this.stepBgColor[0] = '#4A69BD'
                        break
                    case 1:
                        this.stepBgColor = ["#7ed6df","#7ed6df","#7ed6df"]
                        this.stepBgColor[1] = '#4A69BD'
                        break
                    case 2:
                        this.stepBgColor = ["#7ed6df","#7ed6df","#7ed6df"]
                        this.stepBgColor[2] = '#4A69BD'
                        break
                }
            }
        }
    }
</script>

<style scoped>
a{
    text-decoration: none;
    color:#ffffff;
}
.step{
    display: flex;
    width:100%;
    justify-content: space-around;
    margin-top: 26px;
}

 .step .step1,.step2,.step3{
    width: 230px;
    height: 60px;
    font-size: 20px;
    background-color: #7ed6df;
    transform: skewX(-45deg);
    text-align: center;
    line-height: 60px;
    color: #ffffff;
    border:1px solid #3b569e;
    box-shadow: 2px 6px 10px;
}

 .step .step1:hover,.step2:hover,.step3:hover{
    transition: .76s;
    background-color: #4A69BD;
}
</style>