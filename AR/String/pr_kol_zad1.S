#autor: Imenko Prezimić INDEX ra1234-2015
.section .data
    input_msg: .ascii "Unesite string: \0"
    input_len = .-input_msg

    output_msg: .ascii "Izlaz: \0"
    output_len = .-output_msg

    input: .fill max_len, 1, 42  # Буфер для ввода, размер 30 байт
    output: .fill max_len, 1, 42  # Буфер для ввода, размер 30 байт

    max_len = 30
    
.section .text
.global main


main:
    #ввод 
    movl $4, %eax
    movl $1, %ebx
    movl $input_msg, %ecx
    movl $input_len, %edx
    int $0x80

    # запись в стек(массив)
    # строковый ввод
    movl $3, %eax
    movl $0, %ebx
    movl $input, %ecx
    movl $max_len, %edx
    int $0x80

    movl %eax, output_len
    movl $output, %esi





ispis:
 

	movl $4,%eax
	movl $1,%ebx
	movl $output_msg, %ecx
	movl $output_len, %edx
	int $0x80
	
	movl $4,%eax
	movl $1,%ebx
	movl $output, %ecx
	movl %esi,%edx
	int $0x80
	


kraj:


    movl $1, %eax
    movl $0, %ebx
    int $0x80





    








