#https://gotujmy.pl/forum

*** Settings ***
Library  SeleniumLibrary


*** Variables ***

@{emails}    email1  email2  email3  email4  email5
@{passwords}   pass1  pass2  pass3  pass4  pass5

*** Test Case ***
Registration In Forum
    Open Browser    https://gotujmy.pl/forum   Edge
    run keyword and ignore error  click button   //*[@id="tcf277-permissions-modal"]/div[3]/div/button[2]
    Click Element    //*[@id="navTop"]/nav/ul[1]/li[2]/a
    run keyword and ignore error  click button   //*[@id="tcf277-permissions-modal"]/div[3]/div/button[2]
    capture page screenshot
