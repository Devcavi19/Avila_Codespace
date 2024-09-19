section .data
    prompt db 'Enter a message: ', 0
    input_format db '%s', 0

section .bss
    userInput resb 100    ; Buffer to store user input

section .text
    global _main
    extern _printf
    extern _scanf

_main:
    ; Display a prompt
    push prompt
    call _printf
    add esp, 4

    ; Read user input
    push userInput
    push input_format
    call _scanf
    add esp, 8

    ; Display the entered text
    push userInput
    call _printf
    add esp, 4

    ret