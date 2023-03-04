*** Settings ***
Library  SeleniumLibrary
Test Setup     Open My Browser
*** Variables ***
@{emails}  email1@wp.pl  email2@wp.pl  email3@wp.pl  email4@wp.pl  email5@wp.pl
@{passwords}  pass1  pass2  pass3  pass4  pass5
*** Keywords ***
Open My Browser
    Open Browser    https://gotujmy.pl/forum/  Chrome  #executable_path=C:/chromedriver/chromedriver.exe
    maximize browser window
    Execute JavaScript   document.body.style.zoom='50%'
    scroll element into view    //*[@id="tcf277-permissions-modal"]/div[3]/div/button[2]
    run keyword and ignore error  click button    //*[@id="tcf277-permissions-modal"]/div[3]/div/button[2]

Registration In Forum
    [Arguments]  ${email}  ${password}
    click element    //*[@id="navTop"]/nav/ul[1]/li[2]/a
    Sleep  3
    run keyword and ignore error  click button    //*[@id="tcf277-permissions-modal"]/div[3]/div/button[2]
    Sleep  3
    input text    //*[@id="f_cmu_email"]    ${email}
    input text    //*[@id="f_cmu_email2"]    ${email}
    input text    //*[@id="f_cmu_password"]    ${password}
    input text    //*[@id="f_cmu_password2"]    ${password}
    Checkbox Should Not Be Selected  //*[@id="newsletter_agree"]
    select checkbox  //*[@id="newsletter_agree"]
    Checkbox Should Not Be Selected  //*[@id="user_register_form"]/fieldset/label[2]/input
    select checkbox  //*[@id="user_register_form"]/fieldset/label[2]/input
    Checkbox Should Not Be Selected  //*[@id="user_register_form"]/fieldset/label[3]/input
    select checkbox  //*[@id="user_register_form"]/fieldset/label[3]/input
    run keyword and ignore error  click button  //*[@id="user_register_form"]/fieldset/footer/button
    capture page screenshot    #${project_path}/screen1.png
*** Test Cases ***
Registration
    FOR  ${i}  IN RANGE  1
        Registration In Forum  ${emails}[${i}]  ${passwords}[${i}]
        Log    User ${emails}[${i}]
    END