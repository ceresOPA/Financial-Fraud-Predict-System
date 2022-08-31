<template>
    <div class="container">
        <div class="userinfo">
            <div class="account inp-block">原密码：<input v-model="old_password" type="password" class="inp" ></div>
            <div class="username inp-block">新密码：<input v-model="new_password" type="password" class="inp"></div>
            <el-button type="primary" plain style="margin:12px 26px;" @click="changePassword">确认修改</el-button>
        </div>
    </div>
</template>

<script>

    import { UserFilled } from '@element-plus/icons-vue'
    import {Msg} from '../../utils/msg.js'
    import { ElMessageBox } from 'element-plus'

    import axios from '../../req.js'
    
    export default {
        data(){
            return {
                account:"",
                old_password:"",
                new_password:""
            }
        },
        mounted(){
            let user = JSON.parse(localStorage.user)
            this.account = user.account
        },
        methods:{
            changePassword(){
                 let that = this
                 let r = ElMessageBox.confirm('确认修改密码吗?',{
                     confirmButtonText:'确认',
                     cancelButtonText:'取消'
                 }).then(()=>{
                     console.log("success")
                     axios({
                         method:'post',
                         url:'./api/changepassword',
                         data:{
                             account:that.account,
                             old_password:that.old_password,
                             new_password:that.new_password
                         }
                     }).then(res=>{
                         console.log(res.data)
                         if(res.data.state == 'success'){
                            localStorage.setItem('user',JSON.stringify(res.data.info))
                            console.log(res.data.info)
                            Msg("修改成功","success")
                         }else{
                            Msg(res.data.msg,"error")
                         }
                     })
                 }).catch(()=>{})
            }
        },
        components:{
            UserFilled
        }
    }

</script>

<style scoped>
.container{
    display: flex;
    justify-content: center;
    align-items: center;
}

.container .userinfo{
    display: flex;
    flex-direction: column;
    margin-top: 66px;
}

.container .userinfo .avatar{
    text-align: center;
    margin-bottom: 16px;
}

.inp-block{
    margin: 12px 0px;
    margin-right: 30px;
}

.inp{
    padding: 12px 26px;
}


</style>