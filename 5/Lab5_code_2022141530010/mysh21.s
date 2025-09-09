section .text
  global _start
    _start:
	BITS 32
	jmp short two
    one:
 	pop esi
 	xor eax, eax
 	mov [esi+12], al
 	mov [esi+14], al
 	mov [esi+19], al
 	mov [esi+24], al
 	mov [esi+25], esi
 	lea ebx, [esi+13] 
 	mov [esi+29],ebx
 	
 	lea ebx, [esi+15] 
 	mov [esi+33],ebx
 	
 	lea ebx, [esi+20] 
 	mov [esi+37],ebx
 	
 	mov [esi+41],eax
 	
 	mov al,0x0b
 	mov ebx,esi
 	
 	lea ecx,[esi+25]
 	lea edx,[esi+41]
 	int 0x80
     two:
 	call one
 	db '/usr/bin/env*-*a=11*b=22*AAAABBBBCCCCDDDDEEEE' 
