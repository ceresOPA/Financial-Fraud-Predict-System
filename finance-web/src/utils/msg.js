import { ElMessage } from 'element-plus'

export function Msg(msg,type){
    ElMessage({
        message:msg,
        type:type,
        duration:800,
        center: true
    })
}