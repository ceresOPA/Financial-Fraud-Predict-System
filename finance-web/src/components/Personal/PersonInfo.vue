<template>
    <div class="container">
        <div class="userinfo">
            <el-upload
                action="./api/upload"
                :show-file-list="false"
                :on-success="handleAvatarSuccess"
                class="avatar"
            >
                <el-avatar v-if="avatar_url!=''" :src="avatar_url"  ></el-avatar>
                <el-avatar v-else >头像</el-avatar>
            </el-upload>
            <!-- <div @click="upload_avatar" class="avatar">
                <el-avatar v-if="avatar_url!=''"  :src="avatar_url"></el-avatar>
                <input type="file" hidden="true" name="" id="">
            </div> -->
            <div class="account inp-block">账号：<input v-model="account" type="text" class="inp" disabled></div>
            <div class="username inp-block">昵称：<input v-model="username" type="text" class="inp"></div>
            <!-- <div class="password inp-block">密码：<input v-model="password" type="password" class="inp"></div> -->
            <el-button type="primary" plain style="margin:12px 26px;" @click="changeInfo">确认修改</el-button>
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
                username:"",
                password:"",

                avatar_url:""
            }
        },
        mounted(){
            let user = JSON.parse(localStorage.user)
            this.account = user.account
            this.username = user.username
            console.log(user)
            this.avatar_url = user.avatar_url
            if(this.avatar_url!=""&&this.avatar_url.indexOf('/')==-1){
                this.avatar_url = './api/uploads/'+user.avatar_url
            }
        },
        methods:{
            handleAvatarSuccess(res, file, fileList){
                if(res.state == 'success'){
                    Msg("上传成功","success")
                    this.avatar_url = './api/uploads/'+res.info.filename

                }else{
                    Msg(res.msg,'error')
                }
                
            },
            changeInfo(){
                 let that = this
                 let r = ElMessageBox.confirm('确认修改个人信息吗?',{
                     confirmButtonText:'确认',
                     cancelButtonText:'取消'
                 }).then(()=>{
                     console.log("success")
                     axios({
                         method:'post',
                         url:'./api/updateinfo',
                         data:{
                             account:that.account,
                             username:that.username,
                             avatar_url:that.avatar_url.split('/')[3]
                         }
                     }).then(res=>{
                         console.log(res.data)
                         if(res.data.state == 'success'){
                            localStorage.setItem('user',JSON.stringify(res.data.info))
                            console.log(res.data.info)
                            Msg("修改成功","success")
                            this.$router.go('/personal/personalInfo')
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