
/*
 * ws2812.S
 *
 * Created: 15/06/2018 22:44:12
 *  Author: Marcos
 */ 

// R24-25: RGB color pointer
// R23: free
// R22: pixel count
// R20-21: I/O port
// R19: free
// R18: I/O port bit mask

#include "config.h"

.global ws2812_send

ws2812_send:
	// Move data pointer to Z
	movw r30, r24

	// Move SFR pointer to X
	movw r26, r20

	// Make bit clear mask from bit mask
	mov r19, r18
	com r19

	// Set low for 50us
	cli
	ld r20, X
	and r20, r19
	st X, r20
	sei

#if F_CPU == 8000000
    ldi  r20, 133
L1: dec  r20
    brne L1
#elif F_CPU == 16000000
    ldi  r20, 2
    ldi  r21, 9
L1: dec  r21
    brne L1
    dec  r20
    brne L1
#endif

	// If no pixels remaining, just quit
	cp r22, r1
	breq ws2812_send_exit

ws2812_send_next:
	// r20 contains R and r21 contains G
	ld r20, Z+
	ld r21, Z+

	// Time-critical section - disabling interrupts
	cli

	// R24 = port with bit set
	ld r24, X
	or r24, r18

	// R25 = port with bit clear
	mov r25, r24
	and r25, r19

	// Send green
	rcall ws2812_send_byte

	// Send red
	mov r21, r20
	rcall ws2812_send_byte

	// Send blue
	ld r21, Z+
	rcall ws2812_send_byte

	// Re-enable interrupts
	sei

	// Decrement pixel count
	dec r22
	brne ws2812_send_next

ws2812_send_exit:

	ret

ws2812_send_byte:
	ldi r23, 8
ws2812_send_bit:

#if F_CPU == 8000000
	// Zero: 3 cycles up, 7 cycles down
	// One: 6 cycles up, 4 cycles down

	// 0 / 0
	st X, r24
	// 2 / 2

	// 2 / 2
	sbrs r21, 7
	// 3 / 4
	
	// 3 / 4
	st X, r25
	// 5 / 4

	// 5 / 4
	lsl r21
	// 6 / 5

	// 6 / 5
	brcc ws2812_next_bit
	// 8 / 6

	// 8 / 6
	st X, r25
	// 8 / 8

#else
#	error "Unsupported F_CPU"
#endif

ws2812_next_bit:
	// 8 / 8
	dec r23 // 1 cycle
	// 9 / 9

	// 9 / 9
	brne ws2812_send_bit
	// 11 / 11

	ret
