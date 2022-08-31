<template>
    <div class="login-container">
        <div class="banner">
            <img src="/money.png" class="logo">
            <span class="title">金融反欺诈预测系统</span>
        </div>
        <div class="login" >
            <div class="title">
                <img @click="this.$router.push('/login')" src="/return.png" style="width:22px;height:22px;position:absolute;left:16px;top:36px;cursor:pointer;" alt="">
                <span>用户注册</span>
                </div>
            <div class="inp">
                <div class="account">
                    <span style="margin-right:39px;">账号：</span>
                    <input type="text" class="detail-inp" v-model="account" >
                </div>
                <div class="pwd">
                    <span style="margin-right:39px;">密码：</span>
                    <input type="password" class="detail-inp" v-model="password" >
                </div>
                <div class="confirm-pwd">
                    <span>确认密码：</span>
                    <input type="password" class="detail-inp" v-model="confirm_password">
                </div>
            </div>
            <div class="btn">
                <button @click="register" class="register-btn">注册/登录</button>
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
    name:'Register',
    data(){
        return {
            account:"",
            password:"",
            confirm_password:""
        }
    },
    methods:{
        register(){
            let that = this
            if(that.account.trim()==''){
                Msg("请输入账号","error")
                return
            }
            if(that.password.trim()==''){
                Msg("请输入密码","error")
                return
            }
            if(that.confirm_password!=that.password){
                Msg("两次密码不匹配","error")
                return
            }
            let account = that.account.trim()
            let password = that.password.trim()
            axios({
                method:'post',
                url:'/api/register',
                data:{
                    account,
                    password
                }
            }).then(res=>{
                let data = res.data
                if(data.state=='fail'&&data.msg!=undefined){
                    Msg(data.msg,"error")
                }else if(data.state=='success'){
                    let info = data.info
                    Msg("欢迎你,"+info.username,"success")
                    localStorage.setItem('user',JSON.stringify(info))
                    this.$router.push("/")
                }
            })
            // this.$router.push('/yule')
        }
    }
}
</script>

<style scoped>
.login-container{
    height: 100%;
    width:100%;
    position:absolute;
    background-color: #abb5d0;
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
    background: rgba(156, 167, 198, 0.35);
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
    height: 120px;
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
}

.btn .login-btn{
    cursor: pointer;
}

.btn .register-btn{
    width: 160px;
    height: 36px;
    border-radius: 10px;
    border: none;
    margin-left: 18px;
    background-color: #82ccdd;
    color:#ffffff;
}


.btn .register-btn:hover{
    background-color: #69b2cc;
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