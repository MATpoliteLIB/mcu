#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include "pico/stdlib.h"

#ifndef LED_DELAY_MS
#define LED_DELAY_MS 250
#endif

int pico_led_init(void) {   // Инициализация LED
    gpio_init(PICO_DEFAULT_LED_PIN); // инициализация LED, обычно GPIO 25
    gpio_set_dir(PICO_DEFAULT_LED_PIN, GPIO_OUT); // Установка пина на выход, вход (номер пина, вход или выход)
    return PICO_OK;
}

void pico_set_led(bool led_on) {  // Установка определённого bool на выход LED
    gpio_put(PICO_DEFAULT_LED_PIN, led_on);
}

static void read_register(uint8_t *mem_location) {
    uint8_t byte = *mem_location;
    printf("0x%p -> 0x%X", mem_location, byte);
}

int main() {
    stdio_init_all();
    int rc = pico_led_init();
    hard_assert(rc == PICO_OK); // Проверка выполнения программы
    uint8_t *test_addr = (uint8_t *)0x20001000;
    *test_addr = 0xAB;

    while (true) {
        char cmd = getchar(); // как я понял - считывание значения с терминала
        if (cmd == 'e') {
            pico_set_led(true);
        }
        else if (cmd == 'd') {
            pico_set_led(false);
        }
        else if (cmd == 'r') {
            char mem_char[11]; // Считываем 10 символов, однако определяем 11 для избежания ошибок
            for (int i = 0; i < 10; i++) {
                mem_char[i] = getchar();
            }
            mem_char[10] = '\0';
            char *endptr;
            unsigned long mem_long = strtoul(mem_char, &endptr, 16); // Преобразование строки в unsigned long; "16" - интепретирование 16-тиричного числа

            if (endptr == mem_char || *endptr != '\0') {
                printf("Ошибка: ввод должен быть шестнадцатеричным числом!\n");
                return 1;
                }

            uint8_t *mem_loc = (uint8_t *)mem_long;
            read_register(mem_loc);
        }
    }
}
