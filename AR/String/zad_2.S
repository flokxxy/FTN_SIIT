#programa yvelicivaet bykvi i ybirajet probeli

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

	cmpb $0,(%esi)
	je kraj
	
	cmpb $'', (%esi)
	je preskoci
	
	cmpb $'a', (%esi)
	jb preskoci
	cmpb $'z', (%esi)
	jmp zamena
	
	
preskoci:
 	incl %esi
 	jmp change_petlja

	
zamena:
	movb (%esi), %al
	subb $32, %al 
	movb %al,(%edi)
	incl %esi
	incl %edi
	jmp change_petlja

	
kraj:
	movl $1,%eax
	movl $0,%ebx
	int $0x80

