#vvod vivod

.section .data
poruka1: .ascii "Unesite ime i prezime: \0"
poruka1_len = .-poruka1

poruka2: .ascii "Vi ste: \0"
poruka2_len = .-poruka2

imeprez: .fill 50,1,42
imeprez_len: .long 0

.section .text
.global main

main:
	movl $4,%eax
	movl $1,%ebx
	movl $poruka1, %ecx
	movl $poruka1_len,%edx
	int $0x80
	
	movl $3,%eax
	movl $0,%ebx
	movl $imeprez,%ecx
	movl $50,%edx
	int $0x80
	
	
	movl %eax, imeprez_len
	
	movl $imeprez,%esi  #string

petlja:
	cmpl $10,(%esi)
	je ispis
	cmpb $'a',(%esi)
	jb preskoci
	cmpb $'z', (%esi)
	jbe malo_slovo
	jmp preskoci
	
malo_slovo:
	subb $32, (%esi)
	
preskoci:	
	incl %esi
	jmp petlja

ispis:
	movl $4,%eax
	movl $1,%ebx
	movl $poruka2, %ecx
	movl $poruka2_len,%edx
	int $0x80
	
	movl $4,%eax
	movl $1,%ebx
	movl $imprez, %ecx
	movl imeprez_len,%edx
	int $0x80
	

kraj:
	movl $1,%eax
	movl $0, %ebx
	int $0x80
