# Reversed check function
def check(a, b):
    """
    pushq   %rbp
    movq    %rsp, %rbp
    movl    %edi, -36(%rbp) -> A
    movl    %esi, -40(%rbp) -> B
    movl    -36(%rbp), %eax
    xorl    -40(%rbp), %eax
    movl    %eax, -4(%rbp) -> C
    movl    -4(%rbp), %eax
    addl    $98, %eax
    movl    %eax, -8(%rbp) -> D
    movl    -8(%rbp), %eax
    notl    %eax
    movl    %eax, %edx
    movl    -40(%rbp), %eax
    addl    %edx, %eax
    movl    %eax, -12(%rbp) -> E
    movl    -12(%rbp), %eax
    xorl    -36(%rbp), %eax
    movl    %eax, -16(%rbp) -> F
    movl    -40(%rbp), %eax
    imull   -4(%rbp), %eax
    cltd
    idivl   -8(%rbp)
    movl    %eax, %edx
    movl    -36(%rbp), %eax
    leal    (%rdx,%rax), %ecx
    movl    -12(%rbp), %edx
    movl    -16(%rbp), %eax
    addl    %edx, %eax
    xorl    %ecx, %eax
    movl    %eax, -20(%rbp) -> result
    cmpl    $-814, -20(%rbp)
    sete    %al
    popq    %rbp
    ret
    """
    c = a ^ b
    d = 98 + c
    e = ~d + b
    f = e ^ a
    answer = a + b * c / d ^ e + f
    return answer == -814

for a in range(500):
    for b in range(500):
        done = False
        if check(a, b):
            print "%d:%d" % (a, b)
            done = True
            break
    if done:
        break

# 160:284
