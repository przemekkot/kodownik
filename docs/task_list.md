~~Wykonać Menu Screen~~
   ~~Main Menu~~
    W nim dodać
      ~~Nauka Button~~
      ~~Test Button~~
      ~~Exit Button~~
  ~~CodeScreen~~
~~Wykonać Code Screen~~
  W nim dodać
    ~~Product Code~~
    ~~Screen Keyboard~~
      W nim dodać
        ~~Guziki~~
    ~~Product Name~~
    ~~Submit Buttons~~
      W nim dodać
        ~~PLU Button~~
        ~~WAGA Button~~
    ~~App Buttons~~
      W nim dodać
        ~~Next Code Button~~
        ~~Back Button~~
Wykonać Result Screen
  W nim dodać
    ~~Test Result~~
    ~~List of anwsers~~
    ~~Result Buttons~~
Test Result ma
  Label z ZALICZONY/OBLANY
  Label z wynikiem
Codes List ma
  Listę wyników
Result Buttons ma
  Repeat button
  Back Button
CODE DISPATCHER ma
  send PRODUCT CHANGE EVENT with product
Product ma
  reprezentować wpis z listy produktów
Product list ma
  generate list of codes if empty list
  pick first
Code ma
  be created when given product
  has to have EQUAL function
Product Code ma
  catch PRODUCT CHANGE EVENT
  reset
  catch CODE CHANGE EVENT
  show CODE
Product Nama ma
  catch PRODUCT CHANGE EVENT
  set product name
Code Manager ma
  catch NEXT PRODUCT EVENT
  pick product
  catch SUBMIT CODE EVENT
  dispatch PRODUCT CHANGE EVENT with curent CODE
  dispatch NEXT PRODUCT EVENT
  dispatch TEST FINISHED EVENT
Screen Keyboard ma
  catch PRODUCT CHANGE EVENT
  make from the code, a list of buttons to press
  make an empty Entered Code
  reset all keyboard buttons
  highlight the first button to has to be pressed
  highlight next button
  catch BUTTON-NUMBER PRESS
  dispatch CODE CHANGE EVENT with ENTERED CODE
Submit buttons ma
  catch PRODUCT CHANGE EVENT
  highlight a proper submit button
  catch CODE CHANGE EVENT
  save ENTERED CODE
  dispatch SUBMIT CODE EVENT
    with BUTTON
    and
    with ENTERED CODE
Result Screen ma
  display list od CODES and ENTERED CODES
    display
    good out of X
    green
    ok
    red
    bad
Submit Code Event ma być
  wysyłany przez
  odbierany przez
Next Product Event ma być
  wysyłany przez
  odbierany przez
Product Change Event ma być
  wysyłany przez
  odbierany przez
Code Change Event ma być
  wysyłany przez
  odbierany przez
Test Finished Event ma być
  wysyłany przez
  odbierany przez



Nauka ma działać tak
Egzamin na działać tak
Enter Code Workflow ma działać tak
Rzeczy mają

    click on
      Test Button
      runs
      Test Mode
      Nauka Button
      runs
      Nauka Mode
      Exit Button
      exits
      Application
    Screen Keyboard
      shows
        number buttons
        first number of code highlighted
      press on
        keyboard key
        enters
        number
        to
        Code Number
      click on
        number button
        enters
        number
        to
        Code Number



        number button
        not highlighted
        resets
        Code Number and Keyboard
        in
        Nauka Mode


        number button
        highlighted
        adds
        nubmer
        to
        Code Number
        in
        Nauka Mode

    Code Name
      shows
        Product Name
      takes
        Product Name
    Code Number
      shows entered numbers of code
      takes
        code number
      highlight  on green when
        code is good
      highlight  on red when
        code is bad
    Application Buttons
      has
        Back Button




        Next Code Button
        hidden in
        Test Mode
        on
        Result Screen
      click on
        Back Button
        takes to
        Menu


        Next Code Button
        picks
        new Code
        resets
        Code Name, Code Number, Screen Keyboard

    Submit Buttons
      has
        PLU Button
        Waga Button
      click on
        PLU Button
        submits
        Code
        if
        quantity type == szt
        otherwise
        show Error
        Waga Button
        submits
        Code
        if
        quantity type == kg
        otherwise
        show Error
    Test Result
      shows
        test result
    List of Anwsers
      shows
        list of test codes
        green highlight for ok codes
        red highlight for bad codes

    Repeat test button
      click on
        repeat test
        pick new codes

