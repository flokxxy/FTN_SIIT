
.section .text
.global saberi

saberi:
	pushl %ebp
	movl %esp, %ebp
	subl $4*0, %esp #prostor za lokalne prom
	
	pushl %ebx
	pushl %esi
	pushl %edi
	
	#.....logika program.....
	movl 8(%ebp), %eax   #a
	movl 12(%ebp), %ebx  #b
	
	addl %ebx, %eax #povratna vrednost u eax
	
	

kraj_saberi:
	popl %edi
	popl %esi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
	
