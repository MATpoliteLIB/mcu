#include <stdio.h>
#include <stdlib.h>
#include "pico/stdlib.h"
#include "hardware/spi.h"
#include "ili9341/ili9341.h"
#include "TimesNewRoman/TimesNewRoman.h"
#include <string.h>

int main()
{
    stdio_init_all();
    init_SPI();
    init_display();
    init_drawing();
    int humidity = 23;
    char text[32];
    sprintf(text, "HUMIDITY: %d%%", humidity);  

    clear_buffer();
    enter_a_text("0123456789", 100, 100, get_buffer());
    enter_a_text(text, 80, 110, get_buffer());
    display_buffer();
}
