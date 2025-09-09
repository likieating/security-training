section .text
  global _start
    _start:
      ; Store the argument string on stack
      xor  eax,eax
      push eax          ; Use 0 to terminate the string
      push "//sh"
      push "/bin"
      mov  ebx, esp     ; Get the string address
      
      mov edx,"-caa"
      shl edx,16
      shr edx,16
      
      push eax
      push edx
      mov ecx,esp
      
      push eax
      push " -la"
      push "ls  "
      mov edx,esp
      push eax
      push edx
      push ecx
      push ebx
      
      
      mov ecx,esp
      xor edx,edx
      xor eax,eax
      mov al,0x0b
      int 0x80
      

