<template>
    <div class="login-container">
        <div class="banner">
            <img src="/money.png" class="logo">
            <span class="title">金融反欺诈预测系统</span>
        </div>
        <div class="login" >
            <div class="title">用户登录</div>
            <div class="inp">
                <div class="account">
                    <span>账号：</span>
                    <input type="text" v-model="account" class="detail-inp">
                </div>
                <div class="pwd">
                    <span>密码：</span>
                    <input type="password" v-model="pwd" class="detail-inp">
                </div>
            </div>
            <div class="btn">
                <button @click="login" class="login-btn">登录</button>
                <button @click="register" class="register-btn">注册</button>
            </div>
        </div>
        <div class="pic">
            <img src="/index1.png" class="leftpic">
            <img src="/index2.png" class="rightpic">
        </div>
    </div>
</template>

<script>
import axios from '../req.js'
import {Msg} from '../utils/msg.js'

export default {
    name:'Login',
    data(){
        return {
            isLogin:true,
            account:"",
            pwd:""
        }
    },
    methods:{
        login(){
            let that = this
            if(that.account.trim()==''){
                Msg("请输入账号","error")
                return
            }
            if(that.pwd.trim()==''){
                Msg("请输入密码","error")
                return
            }
            axios({
                method: 'post',
                url: '/api/login',
                data:{
                    account:that.account,
                    password:that.pwd
                }
            }).then(res=>{
                let data = res.data
                console.log(data)
                if(data.state == 'fail'){
                    if(data.msg != undefined){
                        Msg(data.msg,"error")
                    }
                }else{
                    let info = data.info
                    Msg("欢迎你,"+info.username,"success")
                    localStorage.setItem('user',JSON.stringify(info))
                    this.$router.push("/")
                }
            });
        },
        register(){
            this.$router.push('/register')
        }
    }
}
</script>

<style scoped>
.login-container{
    height: 100%;
    width:100%;
    position:absolute;
    background-color: #4a69bd;
    display: flex;
    justify-content: center;
    font-family: '楷体';
    align-items: center;
    flex-direction: column;
}

.login-container .banner{
    position: absolute;
    top: 20px;
    left: 80px;
    display: flex;
}

.banner .title{
    font-size: 36px;
    color:#ffffff;
    font-family: '黑体';
}

.banner .logo{
    margin-top: 26px;
    margin-right: 16px;
    width:50px;
    height: 50px;
}

.login-container .login{
    width: 432px;
    height: 360px;
    position: relative;
    background: inherit;
    box-shadow: 0px 0px 8px #333;
    border-radius: 8%;
    z-index: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 100px;
}

.login-container .login::before{
    content: '';
    position: absolute;
    top:0;
    right: 0;
    bottom: 0;
    left: 0;
    background: inherit;
    background-attachment: fixed;
    filter: blur(200px);
    z-index: -1;
}

.login-container .login::after{
    content: '';
    position: absolute;
    top:0;
    right: 0;
    bottom: 0;
    left: 0;
    background: rgba(74,105,189,.35);
    z-index: -1;
}

.title{
    font-size: 36px;
    font-weight: bold;
    color:#ffffff;
    margin-top: 30px;
}

.inp{
    margin-top: 36px;
    margin-right: 52px;
    display: flex;
    flex-direction: column;
    align-items: baseline;
    color: #ffffff;
    font-size: 20px;
    height: 80px;
    justify-content: space-around;
}

.detail-inp{
    padding: 5px;
    font-size: 16px;
    width:200px;
    border-radius: 5px;
    border:0;
    outline: none;
}

.btn{
    margin-top: 36px;
    display: flex;
    width: 100%;
    justify-content: center;
}

.btn .login-btn{
    width: 100px;
    height: 36px;
    border-radius: 10px;
    border: none;
    margin-right: 18px;
    background-color: #82ccdd;
    color:#ffffff;
}

.btn .login-btn:hover{
    background-color: #69b2cc;
    cursor: pointer;
}

.btn .register-btn{
    width: 100px;
    height: 36px;
    border-radius: 10px;
    border: none;
    margin-left: 18px;
}

.btn .register-btn{
    cursor: pointer;
}

.pic .leftpic{
    width:420px;
    height: 420px;
    position: absolute;
    left: 10px;
    bottom: 10px;
}

.pic .rightpic{
    width:420px;
    height: 380px;
    position: absolute;
    right: 10px;
    bottom: 22px;
}

</style>y