; [0] Exit
; [1] Add
; [2] Subtract
; [3] Multiply
; [4] Divide
; Enter choice:

section .data
    prompt db 'Enter choice: ', 0
    num1 db 'Enter first number: ', 0
    num2 db 'Enter second number: ', 0
    result db 'Result: ', 0
    newline db 10, 0

section .bss
    choice resb 1
    number1 resb 4
    number2 resb 4
    res resb 4

section .text
    global _start

_start:
    ; Print prompt
    mov edx, len prompt
    mov ecx, prompt
    call print_string

    ; Read choice
    call read_char
    mov [choice], al

    ; Get first number
    mov edx, len num1
    mov ecx, num1
    call print_string
    call read_number
    mov [number1], eax

    ; Get second number
    mov edx, len num2
    mov ecx, num2
    call print_string
    call read_number
    mov [number2], eax

    ; Perform operation
    mov al, [choice]
    sub al, '0'
    cmp al, 0
    je exit
    cmp al, 1
    je add
    cmp al, 2
    je subtract
    cmp al, 3
    je multiply
    cmp al, 4
    je divide

exit:
    mov eax, 1
    int 0x80

add:
    mov eax, [number1]
    add eax, [number2]
    jmp print_result

subtract:
    mov eax, [number1]
    sub eax, [number2]
    jmp print_result

multiply:
    mov eax, [number1]
    imul eax, [number2]
    jmp print_result

divide:
    mov eax, [number1]
    cdq
    idiv dword [number2]
    jmp print_result

print_result:
    mov [res], eax
    mov edx, len result
    mov ecx, result
    call print_string
    call print_number
    mov edx, len newline
    mov ecx, newline
    call print_string
    jmp exit

print_string:
    mov eax, 4
    mov ebx, 1
    int 0x80
    ret

read_char:
    mov eax, 3
    mov ebx, 0
    mov edx, 1
    int 0x80
    ret

read_number:
    ; Implementation to read a number from stdin
    ; and convert it to an integer in eax
    ; (left as an exercise)
    ret

print_number:
    ; Implementation to print the number in eax
    ; (left as an exercise)
    ret