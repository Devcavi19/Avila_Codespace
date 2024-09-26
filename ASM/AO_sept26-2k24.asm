section .data
   sum db "sum _ %d", 10, 0
   dif db "diff _ %d", 10, 0
   prod db "prod _ %d", 10, 0
   qout db "qout _ %d", 10, 0

section .text
   global _main
   extern _printf

_main:
   mov eax, 30
   mov ebx, 22
   add eax, abx
   push eax
   push sum
   call _printf
   add esp, 8

   ; Substraction
   mov eax, 30
   mov ebx, 22
   sub eax, ebx
   push eax
   push diff
   call _printf
   add esp, 8

   ; Multiplication
   mov eax, 6
   mov ebx, 9
   mul ebx
   push eax
   push prod
   call _printf
   add esp, 8

   ; Division
   mov eax, 16
   mov ebx, 8
   div ebx
   push eax
   push qout
   call _print
   add esp, 8


; sample output: sum = 52
; sample output: diff = 8
; sample output: prod = 54
; sample output: qout = 2
