#include <stdint.h>

void print_u128(uint32_t *a);

void increment_u128(uint32_t *out, uint32_t *a);

void xor_operator_u128(uint32_t *out, uint32_t *a, uint32_t *b);

void and_operator_u128(uint32_t *out, uint32_t *a, uint32_t *b);

void or_operator_u128(uint32_t *out, uint32_t *a, uint32_t *b);

void not_operator_u128(uint32_t *out, uint32_t *a);

void twos_complement_u128(uint32_t *out, uint32_t *a);

void add_u128(uint32_t *out, uint32_t *a, uint32_t *b);

void decrement_u128(uint32_t *out, uint32_t *a);

int greater_u128(uint32_t *a, uint32_t *b);

int less_u128(uint32_t *a, uint32_t *b);

int equal_u128(uint32_t *a, uint32_t *b);

int not_equal_u128(uint32_t *a, uint32_t *b);

void sub_u128(uint32_t *out, uint32_t *a, uint32_t *b);

void left_shift_u128(uint32_t *out, uint32_t *a);

void right_shift_u128(uint32_t *out, uint32_t *a);

void left_rotate_u128(uint32_t *out, uint32_t *a);

void right_rotate_u128(uint32_t *out, uint32_t *a);

void mult_u128(uint32_t *out, uint32_t *a, uint32_t *b);

void div_u128(uint32_t *out, uint32_t *a, uint32_t *b);