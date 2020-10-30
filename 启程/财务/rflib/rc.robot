*** Settings ***
Library  SeleniumLibrary
Variables  conf/cfg.py

*** Keywords ***
loginWebSite
    go to  ${MgrLoginUrl}

    #输入用户名密码
#    input text  id="username"   auto
#    input text  id="password"   sdfsdfsdf
    click element   css=.btn-success

addCourse
    [Arguments]     ${name}     ${desc}     ${idx}
    #进入课程界面
    click element  css=[ui-sref="course"]
    #添加课程
    click element   css=[ng-click="showAddOne=true"]
    input text  css=[ng-model="addData.name"]   ${name}
    input text  css=[ng-model="addData.desc"]   ${desc}
    input text  css=[ng-model="addData.display_idx"]    ${idx}
    # 点击确定创建按钮
    click element   css=[ng-click="addOne()"]
    sleep  1

checkCourse
    [Arguments]     @{expect}
    #进入课程界面
    click element  css=[ui-sref="course"]
    # 检查课程
    ${courses}   get webelements     css=tr td:nth-child(2)
    ${actrual}   evaluate    [course.text for course in $courses]
    log to console  ${actrual}
    # 处理预期结果数据类型 -
    ${exp}  evaluate  [name for name in $expect]
    should be true      $actrual==$exp

deleteAllLesson
    #进入课程界面
    click element  css=[ui-sref="course"]
    #开始删除课程
    set selenium implicit wait    2

    FOR   ${one}   IN RANGE   9999
        ${del_btns}   get webelements    css=[ng-click="delOne(one)"]
        #循环终止条件？课程删除完，删除按钮为空
        exit for loop if    $del_btns==[]
        #点击删除按钮
        click element   ${del_btns}[0]
        #点击确定按钮
        click element   css=.btn-primary
        #等待弹出框消失
        sleep  1
    END

deleteallTeachers

    #切换到老师界面
    click element  css=[ui-sref="teacher"]
    #开始删除老师
    set selenium implicit wait    2

    FOR   ${one}   IN RANGE   9999
        ${del_btns}   get webelements    css=[ng-click="delOne(one)"]
        #循环终止条件？老师删除完，删除按钮为空
        exit for loop if    $del_btns==[]
        #点击删除按钮
        click element   ${del_btns}[0]
        #点击确定按钮
        click element   css=.btn-primary
        #等待弹出框消失
        sleep  1
    END

addTeacher
    [Arguments]   ${realname}   ${username}   ${desc}   ${idx}  ${cousre}
    #切换到老师界面
    click element  css=[ui-sref="teacher"]
    #添加teacher
    click element  css=[ng-click="showAddOne=true"]
    input text   css=[ng-model="addEditData.realname"]   ${realname}
    input text   css=[ng-model="addEditData.username"]   ${username}
    input text   css=[ng-model="addEditData.desc"]   ${desc}
    input text  css=[ng-model="addEditData.display_idx"]   ${idx}
    #选择授课信息
    select from list by label   css=[ng-model*="courseSelected"]   ${cousre}
    #点击加号
    click element  css=[ng-click="addEditData.addTeachCourse()"]
    click element  css=[ng-click="addOne()"]
    sleep  1


checkTeacher
    [Arguments]    @{expect}
    #切换到老师界面
    click element  css=[ui-sref="teacher"]
    #检查老师
    ${teachers}  get webelements   css=tr td:nth-child(3)
    ${actual}  evaluate    [teacher.text for teacher in $teachers]
    log to console  ${actual}
    #处理预期结果数据类型---将传递的多个字符串转化成列表
    ${exp}   evaluate   [name for name in $expect]
    should be true    $actual==$exp

deleteallTrainings

    #切换到培训班界面
    click element  css=[ui-sref="training"]
    #开始删除培训班
    set selenium implicit wait    2

    FOR   ${one}   IN RANGE   9999
        ${del_btns}   get webelements    css=[ng-click="delOne(one)"]
        #循环终止条件？培训班删除完，删除按钮为空
        exit for loop if    $del_btns==[]
        #点击删除按钮
        click element   ${del_btns}[0]
        #点击确定按钮
        click element   css=.btn-primary
        #等待弹出框消失
        sleep  1
    END

addTraining
    [Arguments]   ${realname}   ${desc}   ${idx}  ${cousre}
    #切换到培训班界面
    click element  css=[ui-sref="training"]
    #添加training
    click element  css=[ng-click="showAddOne=true"]
    input text   css=[ng-model="addEditData.name"]   ${realname}
    input text   css=[ng-model="addEditData.desc"]   ${desc}
    input text   css=[ng-model="addEditData.display_idx"]   ${idx}
    #选择包含课
    select from list by label   css=[ng-model="$parent.courseSelected"]   ${cousre}
    #点击加号
    click element  css=[ng-click="addEditData.addTeachCourse()"]
    click element  css=[ng-click="addOne()"]
    sleep  1

checkTraining
    [Arguments]    @{expect}
    #切换到培训班界面
    click element  css=[ui-sref="training"]
    #检查培训班
    ${trainings}  get webelements   css=tr td:nth-child(2)
    ${actual}  evaluate    [training.text for training in $trainings]
    log to console  ${actual}
    #处理预期结果数据类型---将传递的多个字符串转化成列表
    ${exp}   evaluate   [name for name in $expect]
    should be true    $actual==$exp

deleteallGrades

    #切换到培训班界面
    click element  css=[ui-sref="traininggrade"]
    #开始删除培训班
    set selenium implicit wait    2

    FOR   ${one}   IN RANGE   9999
        ${del_btns}   get webelements    css=[ng-click="delOne(one)"]
        #循环终止条件？培训班删除完，删除按钮为空
        exit for loop if    $del_btns==[]
        #点击删除按钮
        click element   ${del_btns}[0]
        #点击确定按钮
        click element   css=.btn-primary
        #等待弹出框消失
        sleep  1
    END

addGrade
    [Arguments]   ${realname}   ${desc}   ${idx}  ${cousre}
    #切换到培训班期界面
    click element  css=[ui-sref="traininggrade"]
    #添加traininggrade
    click element  css=[ng-click="showAddOne=true"]
    input text   css=[ng-model="addEditData.name"]   ${realname}
    input text   css=[ng-model="addEditData.desc"]   ${desc}
    input text   css=[ng-model="addEditData.display_idx"]   ${idx}
    #选择所属培训班
    select from list by label   css=[ng-model="$parent.addEditData.training_id"]   ${cousre}
    #点击确定
    click element  css=[ng-click="addOne()"]
    sleep  1

checkGrade
    [Arguments]    @{expect}
    #切换到培训班期界面
    click element  css=[ui-sref="traininggrade"]
    #检查培训班期
    ${Grades}  get webelements   css=tr td:nth-child(2)
    ${actual}  evaluate    [Grade.text for Grade in $Grades]
    log to console  ${actual}
    #处理预期结果数据类型---将传递的多个字符串转化成列表
    ${exp}   evaluate   [name for name in $expect]
    should be true    $actual==$exp

webtestSetup
    open browser   http://baidu.com     chrome
    set selenium implicit wait  10
    log to console  打开浏览器

webtestTeardown
    close browser
    log to console  关闭浏览器





