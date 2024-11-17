*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kallek
    Set Password  kalle123
    Set Password confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password confirmation  kalle123
    Submit Credentials
    Register ShouldFail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kallek
    Set Password  kalle1
    Set Password confirmation  kalle1
    Submit Credentials
    Register ShouldFail With Message  Password too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kallek
    Set Password  kalleeee
    Set Password confirmation  kalleeee
    Submit Credentials
    Register ShouldFail With Message  Password should contain special characters

Register With Nonmatching Password And Password Confirmation
    Set Username  kallek
    Set Password  kalle123
    Set Password confirmation  kalle1234
    Submit Credentials
    Register ShouldFail With Message  Password and password confirmation don't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password confirmation  kalle123
    Submit Credentials
    Register ShouldFail With Message  Username already taken

Login After Successful Registration
    Set Username  kallek
    Set Password  kalle123
    Set Password confirmation  kalle123
    Submit Credentials
    Go To Login Page
    Set Username  kallek
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kallek
    Set Password  kalle
    Set Password confirmation  kalle
    Submit Credentials
    Go To Login Page
    Set Username  kallek
    Set Password  kalle
    Submit Login Credentials
    Login ShouldFail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page