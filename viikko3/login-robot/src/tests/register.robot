*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  timohehe  timo3210
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  timo  timo3210
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  ti  timo3210
    Output Should Contain  Username should be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  timo10  timo3210
    Output Should Contain  Username should only contain letters (a-z)

Register With Valid Username And Too Short Password
    Input Credentials  timohehe  timo
    Output Should Contain  Password should be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  timohehe  timohehe
    Output Should Contain  Password should contain at least one number or special character

*** Keywords ***
Input New Command And Create User
    Input  new
    Create User  timo  timo1234
