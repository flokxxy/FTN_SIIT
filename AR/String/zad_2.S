.section .data

	str1: .ascii "fhdjjd  gg\0"
	str2: .ascii "***********"

.section .text
.global main

main:
	movl $str1, %esi #pocetak stringa
	movl $0,%ecx #brojac cifra
	movl $str2, %edi
	
	
change_petlja:
	cmpb $'', (%esi)
	je preskoci
	jmp uvel
	
preskoci:
 	incl %esi

uvel:
	cmpb $0,(%esi)
	je kraj
	cmpb $'a', (%esi)
	jb preskoci
	cmpb $'z', (%esi)
	jbe malo_slovo
	jmp zamena
	
zamena:
	movb (%esi), %al
	movb %al,(%edi)
	incl %esi
	incl %edi
	
malo_slovo:
	subb $32, (%esi)


preskoci:
	incl %esi
	jmp petlja 
	
kraj:
	movl $1,%eax
	movl $0,%ebx
	int $0x80

