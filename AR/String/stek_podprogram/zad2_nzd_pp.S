.section .text
.global nzd

nad:
	pushl %ebp
	movl %esp, %ebp
	subl $4*0, %esp
	
	pushl %ebx
	pushl %esi
	pushl %edi
	
	movl 8(%ebp), %eax   #a
	movl 12(%ebp), %ebx  #b
	
	testl  %ebx, %ebx
	je nod_kraj
	
cicle:
	xorl %ecx, %ecx
	divl %edx
	
	


	



nod_kraj:
	popl %edi
	popl %esi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
