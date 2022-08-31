export function changeStepColor(t){
    if(t.$route.path.split('/')[2]=='step1'){
        t.stepBgColor = ["#7ed6df", "#7ed6df","#7ed6df"]
        t.stepBgColor[0] = '#4A69BD'
    }else if(t.$route.path.split('/')[2]=='step2'){
        t.stepBgColor = ["#7ed6df", "#7ed6df","#7ed6df"]
        t.stepBgColor[1] = '#4A69BD'
    }else if(t.$route.path.split('/')[2]=='step3'){
        t.stepBgColor = ["#7ed6df", "#7ed6df","#7ed6df"]
        t.stepBgColor[2] = '#4A69BD'
    }
}