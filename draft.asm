section .data

    message1: db '[1] Addition', 10, 0
    message2: db '[2] Subtraction', 10, 0
    message3: db '[3] Multiplication', 10, 0
    message4: db '[4] Division', 10, 0

    prompt: db 'Enter Choice: ', 0
    input_choice: db '%d', 0

    output: db 'Result is: %d', 10, 0

; Number input
    intInput1: db 'Enter operation 1: ', 0
    op1: db '%d', 0

    intInput2: db 'Enter operation 2: ', 0
    op2: db '%d', 0

section .bss
    entered_num resd 1
    operation1 resd 1
    operation2 resd 1
    result resd 1

section .text

    global _main
    extern _printf
    extern _scanf

_main:
    
    push message1
    call _printf
    add esp, 4

    push message2
    call _printf
    add esp, 4

    push message3
    call _printf
    add esp, 4

    push message4
    call _printf
    add esp, 4

    push prompt
    call _printf
    add esp, 4

    lea eax, [entered_num]
    push eax
    push input_choice
    call _scanf
    add esp, 8

    push intInput1
    call _printf
    add esp, 4

    lea eax, [operation1]
    push eax
    push op1
    call _scanf
    add esp, 8

    push intInput2
    call _printf
    add esp, 4

    lea eax, [operation2]
    push eax
    push op2
    call _scanf
    add esp, 8

    ; Perform the arithmetic operation based on the user's choice
    mov eax, [entered_num]
    cmp eax, 1
    je addition
    cmp eax, 2
    je subtraction
    cmp eax, 3
    je multiplication
    cmp eax, 4
    je division
    jmp end

addition:
    mov eax, [operation1]
    add eax, [operation2]
    mov [result], eax
    jmp print_result

subtraction:
    mov eax, [operation1]
    sub eax, [operation2]
    mov [result], eax
    jmp print_result

multiplication:
    mov eax, [operation1]
    imul eax, [operation2]
    mov [result], eax
    jmp print_result

division:
    mov eax, [operation1]
    cdq
    idiv dword [operation2]
    mov [result], eax
    jmp print_result

print_result:
    push dword [result]
    push output
    call _printf
    add esp, 8

end:
    ret