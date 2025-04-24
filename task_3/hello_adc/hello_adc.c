#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/adc.h"

int main() {
    stdio_init_all();
    
    // Ждём готовности USB (актуально для Windows)
    while (!stdio_usb_connected()) {
        sleep_ms(100);
    }
    printf("Pico готов!\n");

    adc_init();
    adc_gpio_init(26);
    adc_select_input(0);

    while (1) {
        char cmd = getchar(); // Ждём символ
        if (cmd == 'a') {
            const float conversion_factor = 3.3f / (1 << 12);
            uint16_t result = adc_read();
            printf("%f\n", result * conversion_factor); // Отправляем напряжение
            fflush(stdout); // Принудительно сбрасываем буфер
        }
    }
}
