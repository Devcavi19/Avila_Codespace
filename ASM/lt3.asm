; Simple input/output program for asm
; Input name
; input age
; input address 
; output name, age, address
; Nice to meet you, userName, userAge, who lives at userAddress

section .data
    prompt1 db 'Hi! What is your name? : ', 0
    input_name db "%s %s %s", 0

    prompt2 db 'How old are you? : ', 0
    input_age db "%s %s %s", 0

    prompt3 db 'Where do you live? : ', 0
    input_address db "%s %s %s", 0

    output_msg db 'Nice to meet you, %s, who is %s years old and lives at %s', 0

section.bss
    userName resb 100
    userAge resd 100
    userAddress resb 100

section.text
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