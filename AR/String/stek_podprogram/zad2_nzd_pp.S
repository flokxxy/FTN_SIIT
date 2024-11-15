.section .text
.global nzd

nzd:
    pushl %ebp              # Сохраняем старый base pointer
    movl %esp, %ebp         # Устанавливаем новый base pointer
    subl $4*0, %esp           # Зарезервируем место в стеке (не нужно, оставим как 0)

    pushl %ebx              # Сохраняем регистр ebx
    pushl %esi              # Сохраняем регистр esi
    pushl %edi              # Сохраняем регистр edi

    movl 8(%ebp), %eax      # Загружаем первый аргумент (a) в eax
    movl 12(%ebp), %ebx     # Загружаем второй аргумент (b) в ebx

    testl %ebx, %ebx        # Проверяем, равен ли b (ebx) нулю
    je nod_kraj             # Если b == 0, переходим к завершению

cycle:
    xorl %edx, %edx         # Обнуляем регистр edx (для деления)
    divl %ebx               # Делим eax на ebx: eax = a / b, edx = a % b
    movl %ebx, %eax         # Переносим b (ebx) в a (eax)
    movl %edx, %ebx         # Переносим остаток (edx) в b (ebx)
    testl %ebx, %ebx        # Проверяем, равен ли b (ebx) нулю
    jne cycle               # Если b != 0, продолжаем цикл

nod_kraj:
    # В eax находится результат (НОД)
    popl %edi               # Восстанавливаем регистр edi
    popl %esi               # Восстанавливаем регистр esi
    popl %ebx               # Восстанавливаем регистр ebx
    movl %ebp, %esp         # Восстанавливаем стек
    popl %ebp               # Восстанавливаем base pointer
    ret                     # Возвращаемся к вызывающей функции
