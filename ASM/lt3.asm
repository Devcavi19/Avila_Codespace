; Simple input/output program for asm
; Input name
; input age
; input address 
; output name, age, address
; Nice to meet you, userName, userAge, who lives at userAddress

section .data ; section .data is used for declaring initialized data or constants. In our case, we used prompt1, prompt2, prompt3, input_name, input_age, input_address, and output_msg.
    prompt1 db 'Hi! What is your name? : ', 0
    input_name db '%s', 0

    prompt2 db 'How old are you? : ', 0
    input_age db '%s', 0

    prompt3 db 'Where do you live? : ', 0
    input_address db '%s', 0

    output_msg db 'Nice to meet you, %s, who is %s years old and lives at %s', 0

section.bss ; section.bss is where the uninitialized data is stored. We used userName, userAge, and userAddress.
    userName resb 100
    userAge resd 100
    userAddress resb 100

section.text ;  section .text is used for declaring the code or instructions.
    global _main
    extern _printf
    extern _scanf

_main:
    ; Display a prompt1
    push prompt1
    call _printf
    add esp, 4

    ; Read userName input
    push userName
    push input_name
    call _scanf
    add esp, 8

    ; Display prompt2
    push prompt2
    call _printf
    add esp, 4

    ; Read userAge input
    push userAge
    push input_age
    call _scanf
    add esp, 8

    ; Display prompt3
    push prompt3
    call _printf
    add esp, 4

    ; Read userAddress input
    push userAddress
    push input_address
    call _scanf
    add esp, 8

    ; Display the entered text
    push userAddress
    push userAge
    push userName
    push output_msg
    call _printf
    add esp, 16

    ret