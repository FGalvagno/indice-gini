;
; file: inc1.asm
; Subprograma de ejemplo para la interacción con C - Incrementa un valor en 1.

%include "asm_io.inc"

; subrutina suma_uno
; Incrementa el entero pasado como argumento en 1 y almacena el resultado.
; Parámetros:
;   - Entero a incrementar (pasado en EAX)
;   - Puntero a la ubicación de memoria donde se almacenará el resultado (pasado en EBX)
;
; Equivalente en C:
; int suma_uno(int value, int *result) {
;   return value + 1;
; }
;
; Para ensamblar:
; DJGPP:   nasm -f coff inc1.asm
; Borland: nasm -f obj  inc1.asm

segment .text
        global  suma_uno

suma_uno:
        enter   4,0               ; Asigna espacio en la pila para variables locales (aunque no las usemos directamente).
                                  ; Esto crea un frame de pila para fines didácticos.

        push    ebx               ; Guarda EBX, ya que lo usaremos.  IMPORTANTE!


        ; Muestra el frame de pila actual.  Útil para entender cómo se organiza la pila.
        dump_stack 1, 2, 4        ; Imprime el contenido de la pila desde ebp-8 hasta ebp+16
        mov     eax, [ebp+8]      ; eax = n
        mov     ebx, [ebp+12]     ; sum (segundo argumento)
        ; Incrementa el valor en EAX.
        inc     eax

        ; Muestra el frame de pila después de la operación de incremento.
        dump_stack 1, 2, 4        ; Imprime el contenido de la pila desde ebp-8 hasta ebp+16

        ; Almacena el valor incrementado en la dirección apuntada por EBX.
        mov     [ebx], eax

        pop     ebx               ; Restaura EBX.
        leave                      ; Restaura el frame de pila (equivalente a 'mov esp, ebp; pop ebp').
        ret
