section .text
	global start
	extern printf

section .data
thingy1: db 0xb1, 0xd3, 0x32, 0x4c, 0xfc, 0xe6, 0xef, 0x5e, 0xed, 0xe4, 0x66, 0xcd, 0x57, 0xf5, 0xe1, 0x7f, 0xcd, 0x7f, 0x55, 0xf6, 0xe9, 0x64, 0xe7, 0xc9, 0x7f, 0x75, 0xe9, 0x54, 0xe6, 0x4d, 0xf7, 0x79, 0xfc, 0xfc, 0x51, 0x71, 0xf9, 0x3e, 0x18, 0xd9, 0x00

start:
	push   ebp
	mov    ebp,esp
	sub    esp,0x10
	mov    DWORD [ebp-0xc],0x0
	mov    eax,DWORD [ebp+0xc]
	mov    eax,DWORD [eax+0x4]
	mov    DWORD [ebp-0x4],eax
	jmp    part_b
part_a:
	add    DWORD [ebp-0xc],0x1
	add    DWORD [ebp-0x4],0x1
part_b:
	mov    eax,DWORD [ebp-0x4]
	movzx  eax,BYTE [eax]
	test   al,al
	jne    part_a
	mov    DWORD [ebp-0x8],0x0
	jmp    part_d
part_c:
	mov    eax,DWORD [ebp+0xc]
	add    eax,0x4
	mov    edx,DWORD [eax]
	mov    eax,DWORD [ebp-0x8]
	add    eax,edx
	mov    DWORD [ebp-0x4],eax
	mov    eax,DWORD [ebp-0x4]
	movzx  eax,BYTE [eax]
	xor    eax,0xde
	mov    edx,eax
	mov    eax,DWORD [ebp-0x4]
	mov    BYTE [eax],dl
	mov    eax,DWORD [ebp-0x4]
	movzx  eax,WORD [eax]
	ror    ax,0xd
	mov    edx,eax
	mov    eax,DWORD [ebp-0x4]
	mov    WORD [eax],dx
	mov    eax,DWORD [ebp-0x4]
	mov    eax,DWORD [eax]
	rol    eax,0xf
	mov    edx,eax
	mov    eax,DWORD [ebp-0x4]
	mov    DWORD [eax],edx
	add    DWORD [ebp-0x8],0x1
part_d:
	mov    eax,DWORD [ebp-0xc]
	sub    eax,0x3
	cmp    eax,DWORD [ebp-0x8]
	jg     part_c
	mov    eax,DWORD [ebp+0xc]
	mov    eax,DWORD [eax+0x4]
	mov    DWORD [ebp-0x4],eax
	mov    DWORD [ebp-0x10],thingy1
	jmp    part_f
part_e:
	mov    eax,DWORD [ebp-0x4]
	movzx  edx,BYTE [eax]
	mov    eax,DWORD [ebp-0x10]
	movzx  eax,BYTE [eax]
	cmp    dl,al
	je     part_k
	mov    eax,0x0
	jmp    part_h
part_k:
	add    DWORD [ebp-0x4],0x1
	add    DWORD [ebp-0x10],0x1
part_f:
	mov    eax,DWORD [ebp-0x10]
	movzx  eax,BYTE [eax]
	test   al,al
	jne    part_e
	mov    eax,DWORD [ebp+0xc]
	add    eax,0x4
	mov    eax,DWORD [eax]
	mov    edx,DWORD [ebp-0x10]
	mov    ecx,thingy1
	sub    edx,ecx
	add    eax,edx
	movzx  eax,BYTE [eax]
	test   al,al
	je     part_g
	mov    eax,0x0			; LOGIN_FAILED
	jmp    part_h
part_g:
	mov    eax,0x1			; LOGIN_SUCCESS
part_h:
	leave
	ret
