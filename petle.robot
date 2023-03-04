*** Variables ***

${string}    piesek
@{list}    pierwszy    drugi    trzeci    czwarty    piąty
@{list_of_numbers}    1    2    3    4    5
&{dictionary}    slowa=${string}    numer=30    lista=@{list}
@{imiona}   Marcin    Piotr    Ewa    Jan
@{nazwiska}    Kowalski    Nowak    Pan    Coś


*** Test Cases ***
Nest Loops
    @{argument}    Create List    a    b    c    d
    Log    ${argument}          #znowu lista z dolarem, bo potem bedziemy dalej z wypisanymi wartosciami cos robic
    @{numbers}    Create List    ${1}    ${2}   ${3}    ${4}
    Log    ${numbers}
    FOR    ${argumen}    IN    @{argument}
         FOR    ${number}    IN    @{numbers}
             Log    ${argumen} ${number}        #nie uzywamy @ tlyko $ - liste tutaj rozumiemy jako stringa. przez liste rozumiemy calosc z ktorych robimy cos jeszcze
         END
    END

FOR LOOP WITH BREAK
    @{my_list}  create list   Mama    Tata    Pies    Kot    Ptak    I jeszcze cos
    FOR  ${name}   IN   @{my_list}
        IF    $name == 'Pies'    BREAK
        log    ${name}
    END

FOR LOOP WITH CONTINUE
    @{my_list}  create list   Mama    Tata    Pies    Kot    Ptak    I jeszcze cos
    FOR  ${name}   IN   @{my_list}
        IF    $name == 'Pies'    CONTINUE
        log    ${name}
    END

For Loop in Dictionary
    Log    ${dictionary}
    FOR    ${value}    IN    &{dictionary}
        Log    ${value}
    END

For Loop in Range With Index
    FOR    ${i}    IN RANGE    4
        Log    ${imiona}[${i}] ${nazwiska}[${i}]         #nie uzywamy @ tlyko $ - liste tutaj rozumiemy jako stringa. przez liste rozumiem calosc z ktorych robimy cos jeszcze
    END


WHILE LOOP
    ${index}    set variable    10
    WHILE    ${index} > 0
       Log    ${index}0
       ${index}    evaluate    ${index} - 1
    END



For Loop in List
	FOR    ${item}    IN    @{list} #lista jako zbior elementow to @
		Log    ${item}
	END

For Loop in List with IF
	FOR    ${x}    IN    @{list_of_numbers}
		IF   ${x} != 3    Log    ${x}
	END

For Loop In Range 10
	FOR    ${i}    IN RANGE    10
		Log    ${i}
	END

For Loop In Range 4 10
	FOR    ${i}    IN RANGE   4    10
		Log    ${i}
	END

For Loop In Range 4 30 3
	FOR    ${i}    IN RANGE    4    30    3
		Log    ${i}
	END