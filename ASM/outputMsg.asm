section .data
    message db 'Welcome to CS 318!', 10, 0  ; Define the message string

section .text
    extern _printf
    global _main

_main:
        push    message
        call    _printf
        add     esp, 4
        ret