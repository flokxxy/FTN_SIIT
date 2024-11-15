.section .data

	a: .long 3
	b: .long 5
	
.section .text
.global main

main:
	#int saberi(int a,int b)
	pushl b
	pushl a
	call saberi
	
	addl $8, %esp #sklanj
			
	
kraj:
	movl $1,%eax
	movl $0,%ebx
	int $0x80
