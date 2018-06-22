/*
 * LedStrip.c
 *
 * Created: 15/06/2018 18:14:15
 * Author : Marcos
 */ 

#include "config.h"
#include "ws2812.h"
#include <avr/interrupt.h>
#include <avr/io.h>
#include <avr/pgmspace.h>
#include <avr/sleep.h>
#include <util/delay.h>

#define LED_COUNT 4
#define SIN_STEPS 64

static const uint8_t SIN_TBL[SIN_STEPS] PROGMEM = {0, 0, 1, 1, 3, 4, 6, 8, 10, 13, 16, 19, 22, 26, 30, 34, 38, 43, 48, 53, 58, 64, 69, 75, 81, 87, 93, 99, 105, 112, 118, 124, 131, 137, 143, 150, 156, 162, 168, 174, 180, 186, 191, 197, 202, 207, 212, 217, 221, 225, 229, 233, 236, 239, 242, 245, 247, 249, 251, 252, 254, 254, 255, 255};

uint8_t hue = 0;
uint8_t hueSector = 0;

void setupTimer1() {
	cli();
	
	// Clear registers
	TCNT1 = 0;
	TCCR1 = 0;

	// 10.01602564102564 Hz (8000000/((194+1)*4096))
	OCR1C = 194;
	// interrupt COMPA
	OCR1A = OCR1C;
	// CTC
	TCCR1 |= (1 << CTC1);
	// Prescaler 4096
	TCCR1 |= (1 << CS13) | (1 << CS12) | (1 << CS10);
	// Output Compare Match A Interrupt Enable
	TIMSK |= (1 << OCIE1A);

	sei();
}

int main() {
	DDRB = 0b00000001;
	setupTimer1();

	set_sleep_mode(SLEEP_MODE_IDLE);
	sleep_enable();

	while (1) {
		sleep_cpu();
	}
}

ISR(TIMER1_COMPA_vect) {
	struct RgbColor colors[LED_COUNT];
	uint8_t r, g, b;

	switch (hueSector) {
		case 0:
			r = 255;
			g = pgm_read_byte_near(&SIN_TBL[hue]);
			b = 0;
			break;

		case 1:
			r = pgm_read_byte_near(&SIN_TBL[SIN_STEPS - hue - 1]);
			g = 255;
			b = 0;
			break;

		case 2:
			r = 0;
			g = 255;
			b = pgm_read_byte_near(&SIN_TBL[hue]);
			break;

		case 3:
			r = 0;
			g = pgm_read_byte_near(&SIN_TBL[SIN_STEPS - hue - 1]);
			b = 255;
			break;

		case 4:
			r = pgm_read_byte_near(&SIN_TBL[hue]);
			g = 0;
			b = 255;
			break;

		default:
			r = 255;
			g = 0;
			b = pgm_read_byte_near(&SIN_TBL[SIN_STEPS - hue - 1]);
	}


	for (int i = 0; i < LED_COUNT; i++) {
		colors[i].r = r;
		colors[i].g = g;
		colors[i].b = b;
	}
	ws2812_send(colors, LED_COUNT, &PORTB, _BV(0));

	hue++;
	if (hue == SIN_STEPS) {
		hue = 0;
		hueSector++;
		if (hueSector == 6) {
			hueSector = 0;
		}
	}
}
