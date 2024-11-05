.section .data
    ulaz_str: .ascii "Unesite string: \0"
    ulaz_len = .-ulaz_str

    cifra: .byte 0

    unos_max = 50
    unos: .fill unos_max, 1, 42

    out_str: .ascii "result: \0"
    out_len = .-out_str

    rezult: .byte 0

.section .text
.global main

main:
#ввели
    movl $4, %eax
    movl $1, %ebx
    movl $ulaz_str, %ecx
    movl $ulaz_len, %edx
    int $0x80

#прочитали то что ввели макс 50 символов
    movl $3, %eax
    movl $0,%ebx
    leal unos, %ecx
    movl $unos_max,%edx
    int $0x80

    movl %eax, %edi
    decl %edi

    xorl %esi, %esi
    xorl %edx, %edx

cicle:
    cmpl %edi,%esi
    je kraj_str

    cmpl $10, unos(,%esi,1)
    je kraj_str

    movb unos(,%esi,1), %al 
    #загрузка символа кот первый в al

    cmpb $'0', %al
    jb ne_cifra
    cmpb $'9',%al
    ja ne_cifra

#je - сравнение показало равенство
#ja - сравнение показало что правый меньше
#jb - сравнение показало что правый больше

    cmpb $0, cifra
    jne min_max
    movb %al,%bl
    movb %al, %bh
    movb $1, cifra


min_max:
    cmpb %bl, %al
    jmp max
    movb %al,%bh

max:
    cmpb %bh, %al
    jbe ne_cifra
    movb %al, %bh

ne_cifra:
    incl %esi
    jmp cicle

kraj_str:
    cmpb $0, cifra
    jne ekstrem
    movl $0, %ebx
    jmp kraj

ekstrem:
   # addb %bh, %bl
   # xorb %bh, %bh
   movb %bl, rezult



    movl $4,%eax
    movl $1, %ebx
    movl $out_str, %ecx
    movl $out_len, %edx
    int $0x80

    movzx eax, byte [rezult] 
    add eax, '0'        
    mov [unos], al 

    movl $4, %eax
    movl $1, %ebx
    leal unos, %ecx
    #movl $1, %edx            
    int $0x80



kraj:
    movl $1, %edx
    xorb %bh, %bh
    int $0x80




