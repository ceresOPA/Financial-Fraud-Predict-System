import {createRouter,createWebHashHistory} from 'vue-router'

import Login from './components/Login.vue'
import Home from './components/Home.vue'
import Register from './components/Register.vue'

import Step from './components/Step/Step.vue'

import Step1 from './components/Step/Step1.vue'
import Step2 from './components/Step/Step2.vue'
import Step3 from './components/Step/Step3.vue'

import Personal from './components/Personal/Personal.vue'

import PersonInfo from './components/Personal/PersonInfo.vue'
import PredictRecord from './components/Personal/PredictRecord.vue'
import ChangePassword from './components/Personal/ChangePassword.vue'


const router = createRouter({
    history:createWebHashHistory(),
    routes:[
        {
            path:'/',
            component:Home,
            children:[
                {
                    path:'step',
                    component:Step,
                    children:[
                        {
                            path:'step1',
                            component:Step1
                        },      {
                            path:'step2/:filename',
                            component:Step2
                        },  {
                            path:'step2',
                            component:Step2
                        }, 
                          {
                            path:'step3',
                            component:Step3
                        },
                        {
                            path:'step3/:filename',
                            component:Step3
                        }
                    ]
                },
                {
                    path:'/personal',
                    component:Personal,
                    children:[
                        {
                            path:'personalInfo',
                            component:PersonInfo
                        },
                        {
                            path:'predictRecord',
                            component:PredictRecord
                        },
                        {
                            path:'changePassword',
                            component:ChangePassword
                        }
                    ]
                }
            ]
        },
        {
            path:'/login',
            component:Login
        },{
            path:'/register',
            component:Register
        }
    ]
})

export default router