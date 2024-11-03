


.section .data
    input_msg: .ascii "Unesite string: \0"
    input_len = .-input_msg

    output_msg: .ascii "Izlaz: \0"
    output_len = .-output_msg

    max_len = 30
    input: .fill max_len, 1, 0  # Буфер для ввода, размер 30 байт
    output: .fill max_len, 1, 0  # Буфер для вывода, размер 30 байт

.section .text
.global main

main:
    # Ввод строки
    movl $4, %eax         # sys_write
    movl $1, %ebx         # stdout
    movl $input_msg, %ecx # адрес сообщения
    movl $input_len, %edx # длина сообщения
    int $0x80

    # Чтение строки
    movl $3, %eax         # sys_read
    movl $0, %ebx         # stdin
    movl $input, %ecx     # адрес буфера
    movl $max_len, %edx   # максимальная длина
    int $0x80

    # Сохраняем количество прочитанных байтов
    movl $0, %esi       # %esi = длина введенной строки
    movl $output, %eax

cicle:
    cmpb $10, input(%edi) # Если встретили '\n'
    je ispis              # Переходим к выводу

    cmpb $'i', input(%edi) # Если символ 'i'
    je rev

    # Копируем в выходной буфер
    movb input(%edi), output(%ebx)
    inc %ebx              # Увеличиваем индекс output
    jmp next

rev:
    dec %ebx              # Уменьшаем индекс для обратного копирования
    movl %ebx, %edi       # Сохраняем для обратного цикла

cicle_rev:
    cmp %edi, -1          # Если дошли до начала, завершаем
    jl next               # Переходим к следующему
    movb input(%edi), output(%ebx) # Копируем в output
    inc %ebx              # Увеличиваем индекс output
    dec %edi              # Уменьшаем индекс input
    jmp cicle_rev

next:
    inc %edi              # Увеличиваем индекс input
    jmp cicle

ispis:
    movb $0, output(%ebx) # Завершаем строку нулевым символом

    # Вывод сообщения
    movl $4, %eax
    movl $1, %ebx
    movl $output_msg, %ecx
    movl $output_len, %edx
    int $0x80

    # Вывод результата
    movl $4, %eax
    movl $1, %ebx
    movl $output, %ecx
    movl %esi, %edx       # Длина строки для вывода
    int $0x80

kraj:
    movl $1, %eax         # sys_exit
    xorl 0, %ebx       # код выхода 0
    int $0x80
