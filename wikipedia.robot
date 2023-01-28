*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Keywords ***


*** Test Cases ***
Test 1
    Open Browser    https://pl.wikipedia.org    Edge
    Click Element   id:pt-login
    sleep  1
    input text    id:wpName1    lucyna
    sleep  1
    input password    id:wpPassword1    lucyna
    sleep  1
    Click button    id:wpLoginAttempt
    capture page screenshot    screen.png
