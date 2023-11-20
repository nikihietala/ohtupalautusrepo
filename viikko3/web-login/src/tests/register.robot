*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Register User And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  timohehe
    Set Password  timo1234
    Set Password Again  timo1234
    Submit Register Credentials
    Successful Register

Register With Too Short Username And Valid Password
    Set Username  ti
    Set Password  timo1234
    Set Password Again  timo1234
    Submit Register Credentials
    Unsuccessful Register  Username must be at least 3 characters long

Register With Valid Username And Invalid Password
    Set Username  timohoho
    Set Password  timohihi
    Set Password Again  timohihi
    Submit Register Credentials
    Unsuccessful Register  Password must be at least 8 characters long and contain at least one number or special character

Register With Nonmatching Password And Password Confirmation
    Set Username  timohaha
    Set Password  timo1234
    Set Password Again  timo1233
    Submit Register Credentials
    Unsuccessful Register  Password and password confirmation do not match

Login After Successful Registration
    Set Username  mikkohehe
    Set Password  mikko1234
    Set Password Again  mikko1234
    Submit Register Credentials
    Successful Register
    Go To Home Page
    Go To Login Page
    Set Username  mikkohehe
    Set Password  mikko1234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  mikahehe
    Set Password  mika1234
    Set Password Again  mika1233
    Submit Register Credentials
    Unsuccessful Register  Password and password confirmation do not match
    Go To Home Page
    Go To Login Page
    Set Username  mikahehe
    Set Password  mika1234
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register User And Go To Register Page
    Create User  timo  timo1234
    Go To Register Page
    Register Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Again
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Register Credentials
    Click Button  Register

Successful Register
    Title Should be  Welcome to Ohtu Application!

Unsuccessful Register
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
