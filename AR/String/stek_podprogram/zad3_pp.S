.section .text
.global saberi_niz

saberi:
	pushl %ebp
	movl %esp, %ebp
		
	pushl %ebx 
	pushl %esi 
	pushl %edi 
	
	movl 8(%ebp), %eax   #a
	movl 12(%ebp), %ebx  #b
	movl 16(%ebp), %ecx  #c
	
	movl $0, %edi  #greska
	
	
	movl $0, %esi #index
	
cicle:
	cmpl $0, 20(%ebp)  #n


	#movl (%eax), %edx
	movl (%eax, %esi, 8), %edx
	#addl (%ebx), %edx
	addl (%ebx, %esi, 8), %edx
	#movl %edx, (%ecx)
	movl %edx, (%ecx, %esi, 8)
	
	movl 4(%eax), %edx
	adcl 4(%ebx), %edx
	jc greska
	movl %edx, 4(%ecx)
	
	incl %esi
	
	#addl $8, %ax
	#addl $8, %edx
	#addl $8, %ecx
	
	decl 20, %ebp
	
	jmp cicle
	
greska:
	movl $1, %edi
	
kraj:
	ovl %edi, %eax

	popl %edi
	popl %esi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret

	
