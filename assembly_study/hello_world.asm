; hello_world.asm
; author: William Suzuki
; Date: 2021-11-13
; https://www.youtube.com/watch?v=HgEGAaYdABA&ab_channel=JohnHammond
; tutorial based on the video above

global _start

section .text:

_start:
    mov eax, 0x4                    ; use the write syscall
    mov ebx, 1                      ; use stdout as the fd (file descriptor)
    mov ecx, message                ; use the message as the buffer
    mov edx, message_length         ; supply the message length
    int 0x80                        ; int = interrupt, invoke the syscall

    ; ---- now exit the program

    mov eax, 0x1
    mov ebx, 0
    int 0x80

section .data:
    message: db "Hello World!", 0xA
    message_length equ $-message




