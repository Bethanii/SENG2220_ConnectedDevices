	.arch armv6
	.eabi_attribute 28, 1
	.eabi_attribute 20, 1
	.eabi_attribute 21, 1
	.eabi_attribute 23, 3
	.eabi_attribute 24, 1
	.eabi_attribute 25, 1
	.eabi_attribute 26, 2
	.eabi_attribute 30, 6
	.eabi_attribute 34, 1
	.eabi_attribute 18, 4
	.file	"echoDecHex.c"
	.text
	.section	.rodata
	.align	2
.LC0:
	.ascii	"Enter an unsigned decimal integer: \000"
	.align	2
.LC1:
	.ascii	"%u\000"
	.align	2
.LC2:
	.ascii	"Enter a bit pattern in hexadecimal: \000"
	.align	2
.LC3:
	.ascii	"%x\000"
	.align	2
.LC4:
	.ascii	"%u is stored as %#010x, and\012\000"
	.align	2
.LC5:
	.ascii	"%#010x represents the unsigned decimal integer %u\012"
	.ascii	"\000"
	.text
	.align	2
	.global	main
	.arch armv6
	.syntax unified
	.arm
	.fpu vfp
	.type	main, %function
main:
	@ args = 0, pretend = 0, frame = 8
	@ frame_needed = 1, uses_anonymous_args = 0
	push	{fp, lr}
	add	fp, sp, #4
	sub	sp, sp, #8
	ldr	r0, .L3
	bl	printf
	sub	r3, fp, #8
	mov	r1, r3
	ldr	r0, .L3+4
	bl	__isoc99_scanf
	ldr	r0, .L3+8
	bl	printf
	sub	r3, fp, #12
	mov	r1, r3
	ldr	r0, .L3+12
	bl	__isoc99_scanf
	ldr	r3, [fp, #-8]
	ldr	r2, [fp, #-8]
	mov	r1, r3
	ldr	r0, .L3+16
	bl	printf
	ldr	r3, [fp, #-12]
	ldr	r2, [fp, #-12]
	mov	r1, r3
	ldr	r0, .L3+20
	bl	printf
	mov	r3, #0
	mov	r0, r3
	sub	sp, fp, #4
	@ sp needed
	pop	{fp, pc}
.L4:
	.align	2
.L3:
	.word	.LC0
	.word	.LC1
	.word	.LC2
	.word	.LC3
	.word	.LC4
	.word	.LC5
	.size	main, .-main
	.ident	"GCC: (Raspbian 10.2.1-6+rpi1) 10.2.1 20210110"
	.section	.note.GNU-stack,"",%progbits
