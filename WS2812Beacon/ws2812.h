/*
 * ws2812.h
 *
 * Created: 15/06/2018 22:10:03
 *  Author: Marcos
 */ 

#ifndef LEDSTRIP_H_
#define LEDSTRIP_H_

#include <stdint.h>

struct RgbColor {
	uint8_t r;
	uint8_t g;
	uint8_t b;
};

void ws2812_send(const struct RgbColor * values, uint16_t count, volatile uint8_t * ioPort, uint8_t ioBit);

#endif /* LEDSTRIP_H_ */
