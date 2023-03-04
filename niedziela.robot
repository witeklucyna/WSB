*** Settings ***
Library  Collections

*** Variables ***
@{my_list}   1  2  3  4
${zmienna}    4
${slowo}     WSB


*** Test Cases ***
List Basic
    FOR  ${index}    IN    @{my_list}
        Log    ${index}
    END

    append to list    ${my_list}    ${4}       #to oznacza ze jest to in
    append to list    ${my_list}    doopa       #bez {} to string ' '
    append to list    ${my_list}    XD
    append to list    ${my_list}    XD
    append to list    ${my_list}    ${slowo}
    Log    ${my_list}


    ${my_list}    remove duplicates    ${my_list}
    Log    ${my_list}


    remove from list    ${my_list}  0      #wywala wartosc z indexem 0
    Log    ${my_list}


    remove values from list    ${my_list}  2  3      #usuwa konkretne wartosci
    Log    ${my_list}


   list should contain value    ${my_list}    WSB
   Log    ${my_list}