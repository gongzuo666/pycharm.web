*** Settings ***
Library     pylib.WebOpAdmin
Library     pylib.GetTxtData

*** Test Cases ***
添加摘要
    [Setup]    DeleteAbstract
    #新语法
    ${list}    adddata
    #循环头
    FOR  ${one}  IN  @{list}
    #循环体
    log to console  ${one}
    addAbstract     ${one}[number]    ${one}[name]
    #结束循环
    END


