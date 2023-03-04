*** Settings ***
Library      RequestsLibrary

#https://simple-books-api.glitch.me


*** Variables ***
${token}    731187f9917ec1164932415ab0873f84c472620a375a23e1bbf3532b5a50f804
#{
#    "clientName": "Postman",
#    "clientEmail": "valentin@example.com"
#}

*** Test Case ***

API_GET_STATUS
    ${get_response}   GET    https://simple-books-api.glitch.me/status
    Log to console    status ${get_response}


#POST_REGISTRATION
#    ${register_json}    create dictionary    clientName=lucyna    clientEmail=lucyna@example.com
#    ${post_register_json}    POST    https://simple-books-api.glitch.me/api-clients    json=${register_json}


GET_BOOKS

    ${get_response}    GET    https://simple-books-api.glitch.me/books
    Log to console    status ${get_response}



ORDER
   ${headers}    create dictionary    Content-Type=application/json    Authorization=Bearer ${token}
   &{order_body}    create dictionary    bookId=4    ClientName=lucyna
   ${post_order_response}    POST    https://simple-books-api.glitch.me/orders    headers=${headers}
   ...                                                                                       json=&{order_body}

#API_GET_TEST_2
#    ${get_response}=    GET    https://simple-books-api.glitch.me/books
#    Log to console    status ${get_response}

