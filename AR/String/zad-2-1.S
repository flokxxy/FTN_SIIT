
	jmp change_petlja

zamena:
	movb (%esi), %al # загрузка символа
	subb $32, %al # преобразование в заглавную букву
	movb %al, (%edi) # запись в результат
	incl %edi
	incl %esi
	jmp change_petlja

kraj:
	movb $0, (%edi) # завершаем строку
	movl $1, %eax # системный вызов exit
	xorl %ebx, %ebx # код возврата 0
	int $0x80