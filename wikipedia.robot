*** Settings ***
Library  SeleniumLibrary
Test Setup    OPEN WIKIPEDIA
Test Teardown    Close browser

*** Variables ***
${wikipedia_login}    RobotTests
${wikipedia_password}    RobotWorkspace
${error_message}    Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz.
*** Keywords ***
OPEN WIKIPEDIA
    Open Browser    https://pl.wikipedia.org    Edge

Log in Wikipedia
    [Arguments]  ${login}    ${password}
    Open Browser    https://pl.wikipedia.org    Edge
    Click Element   id:pt-login
    Input Text    id:wpName1    ${login}
    Input Password    id:wpPassword1    ${password}
    Click button    id:wpLoginAttempt
    Checkbox Should Not Be Selected    id:wpRemember
    Select Checkbox    id:wpRemember
    click button    id:wpLoginAttempt

*** Test Cases ***
Search_in_Wikipedia
    Open Browser    https://pl.wikipedia.org    Edge
    Input Text    id:searchInput    Lewandowska Anna
    Click button    id:searchButton
    sleep    2
    capture page screenshot    screen.png

Unsuccesfull_Login_to_Wikipedia
    Log in Wikipedia    ${wikipedia_login}    ${wikipedia_password}
    wait until element is visible    css:.mw-message-box-error  timeout=5
    ${my_error_message}    Get Text    css:.mw-message-box-error
    Log    ${my_error_message}
    Log to Console    ${my_error_message}
    Should be equal as strings    ${error_message}    ${my_error_message}
    capture page screenshot    screen2.png
