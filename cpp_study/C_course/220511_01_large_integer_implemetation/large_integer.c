#include <stdio.h>

void print_u128(uint32_t *a)
{
    printf("0x%08x_%08x_%08x_%08x\n", a[3], a[2], a[1], a[0]);
}

void increment_u128(uint32_t *out, uint32_t *a)
{
    uint64_t sum;

    sum = (uint64_t)a[0] + 1;
    out[0] = (uint32_t)sum;

    for (int i = 1; i <= 3; i++)
    {
        sum = (uint64_t)a[i] + (uint64_t)(sum >> 32);
        out[i] = (uint32_t)sum;
    }
}

void xor_operator_u128(uint32_t *out, uint32_t *a, uint32_t *b)
{
    for (int i = 0; i < 4; i++)
    {
        out[i] = a[i] ^ b[i];
    }
}

void and_operator_u128(uint32_t *out, uint32_t *a, uint32_t *b)
{
    for (int i = 0; i < 4; i++)
    {
        out[i] = a[i] & b[i];
    }
}

void or_operator_u128(uint32_t *out, uint32_t *a, uint32_t *b)
{
    for (int i = 0; i < 4; i++)
    {
        out[i] = a[i] | b[i];
    }
}

void not_operator_u128(uint32_t *out, uint32_t *a)
{
    for (int i = 0; i < 4; i++)
    {
        out[i] = ~a[i];
    }
}

void twos_complement_u128(uint32_t *out, uint32_t *a)
{
    uint32_t out_temp_1[5] = {0, 0, 0, 0, 0};

    not_operator_u128(out_temp_1, a);

    increment_u128(out, out_temp_1);
}

void add_u128(uint32_t *out, uint32_t *a, uint32_t *b)
{
    uint64_t sum;

    sum = (uint64_t)a[0] + (uint64_t)b[0];
    out[0] = (uint32_t)sum;

    sum = (uint64_t)a[1] + (uint64_t)b[1] + (uint64_t)(sum >> 32);
    out[1] = (uint32_t)sum;

    sum = (uint64_t)a[2] + (uint64_t)b[2] + (uint64_t)(sum >> 32);
    out[2] = (uint32_t)sum;

    sum = (uint64_t)a[3] + (uint64_t)b[3] + (uint64_t)(sum >> 32);
    out[3] = (uint32_t)sum;

    out[4] = (uint32_t)(sum >> 32);
}

/**
 * @brief Decrement 1 to "a" then outputs it to "out".
 *
 * Decrement by 1 the 128 bit integer that is inserted as argument.
 * Decrement is just an example of subtraction.
 * We achieve this by using addition, and 2's complement.
 * @param out
 * @param a
 */
void decrement_u128(uint32_t *out, uint32_t *a)
{
    uint64_t sum;

    uint32_t a_temp[4] = {1, 0, 0, 0};
    uint32_t neg_one[5] = {0, 0, 0, 0, 0};

    twos_complement_u128(neg_one, a_temp);

    add_u128(out, a, neg_one);
}

/**
 * @brief Returns 1 if "a" is strictly greater than "b". Returns 0 otherwise.
 *
 * @param a
 * @param b
 * @return int
 */
int greater_u128(uint32_t *a, uint32_t *b)
{
    // look how to find greater than using only bitwise operators
    // https://stackoverflow.com/questions/10096599/bitwise-operations-equivalent-of-greater-than-operator
    // https://iq.opengenus.org/bitwise-comparisons/

    uint32_t a_gt_b = 0;
    uint32_t b_gt_a = 0;

    for (int i = 3; i >= 0; i--)
    {
        a_gt_b += (a[i] > b[i]) << i;
        b_gt_a += (a[i] < b[i]) << i;
    }
    // printf("a_gt_b = 0x%0x\tb_gt_a = 0x%x\n", a_gt_b, b_gt_a);

    // uint32_t msb = a_gt_b ^ b_gt_a;
    // msb |= msb >> 1;
    // msb |= msb >> 2;
    // msb |= msb >> 4;
    // msb |= msb >> 8; ...
    // msb |= msb >> 16; ... this in the case of 32 bit integer
    // return !!(a_gt_b & msb)

    // An alternative is to use just bitwise operations
    // but this may not be necessary
    // in our case the restriction is if-else (condition operators)
    // and variable loop

    return (a_gt_b > b_gt_a);
}

/**
 * @brief Returns 0 if "a" is strictly less than "b". Returns 0 otherwise.
 *
 * @param a
 * @param b
 * @return int
 */
int less_u128(uint32_t *a, uint32_t *b)
{
    uint32_t a_gt_b = 0;
    uint32_t b_gt_a = 0;

    for (int i = 3; i >= 0; i--)
    {
        a_gt_b += (a[i] > b[i]) << i;
        b_gt_a += (a[i] < b[i]) << i;
    }

    return (a_gt_b < b_gt_a);
}

/**
 * @brief Returns 1 if "a" and "b" are equal. Returns 0, otherwise.
 *
 * @param a
 * @param b
 * @return int
 */
int equal_u128(uint32_t *a, uint32_t *b)
{

    uint32_t out[5] = {0, 0, 0, 0, 0};

    xor_operator_u128(out, a, b);

    uint32_t holder = 0;
    for (int i = 0; i < 4; i++)
    {
        holder |= out[i];
    }

    return !holder;
}

int not_equal_u128(uint32_t *a, uint32_t *b)
{
    return !equal_u128(a, b);
}

void sub_u128(uint32_t *out, uint32_t *a, uint32_t *b)
{
    uint32_t b_2s_comp[5] = {0, 0, 0, 0, 0};

    twos_complement_u128(b_2s_comp, b);

    add_u128(out, a, b_2s_comp);
}

void left_shift_u128(uint32_t *out, uint32_t *a)
{
}

void right_shift_u128(uint32_t *out, uint32_t *a)
{
}

void left_rotate_u128(uint32_t *out, uint32_t *a)
{
}

void right_rotate_u128(uint32_t *out, uint32_t *a)
{
}

/**
 * @brief Makes all values in the array 0.
 *
 * This is used to reset all values in the 4 positions of the 32 bit array.
 * @param a
 */
void reset_u128(uint32_t *a)
{
    int i;

    for (i = 0; i < 4; i++)
    {
        a[i] = 0;
    }
}

void mult_u128(uint32_t *out, uint32_t *a, uint32_t *b)
{
    reset_u128(out);

    uint32_t holder[4] = {0};
    uint64_t mult;

    mult = (uint64_t)a[0] * (uint64_t)b[0];
    holder[0] = (uint32_t)mult;

    mult = (uint64_t)a[0] * (uint64_t)b[1] + (uint64_t)(mult >> 32);
    holder[1] = (uint32_t)mult;

    mult = (uint64_t)a[0] * (uint64_t)b[2] + (uint64_t)(mult >> 32);
    holder[2] = (uint32_t)mult;

    mult = (uint64_t)a[0] * (uint64_t)b[3] + (uint64_t)(mult >> 32);
    holder[3] = (uint32_t)mult;

    add_u128(out, holder, out);
    reset_u128(holder);

    mult = (uint64_t)a[1] * (uint64_t)b[0];
    holder[1] = (uint32_t)mult;

    mult = (uint64_t)a[1] * (uint64_t)b[1] + (uint64_t)(mult >> 32);
    holder[2] = (uint32_t)mult;

    mult = (uint64_t)a[1] * (uint64_t)b[2] + (uint64_t)(mult >> 32);
    holder[3] = (uint32_t)mult;

    add_u128(out, holder, out);
    reset_u128(holder);

    mult = (uint64_t)a[2] * (uint64_t)b[0];
    holder[2] = (uint32_t)mult;

    mult = (uint64_t)a[2] * (uint64_t)b[1] + (uint64_t)(mult >> 32);
    holder[3] = (uint32_t)mult;

    add_u128(out, holder, out);
    reset_u128(holder);

    mult = (uint64_t)a[3] * (uint64_t)b[0];
    holder[3] = (uint32_t)mult;

    add_u128(out, holder, out);
    reset_u128(holder);
}

/**
 * @brief Divide two uint64_t numbers.
 * If the denominator b is zero we return zero.
 *
 * @param a
 * @param b
 * @return uint64_t
 */
uint64_t safe_divide(uint64_t a, uint32_t b)
{
    if (b == 0)
        return 0;

    return a / b;
}

/**
 * @brief Gives the rest or modulo.
 * To make things easier we make the calculation of the rest given
 * that we already have made the division in a priveous step.
 *
 * @param denominator
 * @param divi
 * @param next_num
 * @return uint64_t
 */
uint64_t safe_rest(uint64_t numerator, uint64_t denominator, uint64_t divi)
{
    uint64_t rest = numerator - denominator * divi;
    return rest;
}

/**
 * @brief Divide two 128 bit unsigned integers.
 * If denominator is 0 then return 0
 *
 * @param out
 * @param a
 * @param b
 */
void div_u128(uint32_t *out, uint32_t *a, uint32_t *b)
{
    reset_u128(out);

    uint32_t holder[4] = {0};
    uint64_t divi;
    uint64_t rest;

    // second proposal of implementation ==========================================================
    divi = safe_divide((uint64_t)a[3], (uint64_t)b[0]);
    holder[3] = (uint32_t)divi;
    rest = safe_rest((uint64_t)a[3], (uint64_t)b[0], divi);

    // divi = safe_divide((rest << 32) + (uint64_t)a[2], (uint64_t)b[0]);
    divi = safe_divide((uint64_t)a[2], (uint64_t)b[0]) + safe_divide((rest << 32), (uint64_t)b[0]);
    holder[2] = (uint32_t)divi;
    rest = safe_rest((rest << 32) + (uint64_t)a[2], (uint64_t)b[0], divi);

    // divi = safe_divide((rest << 32) + (uint64_t)a[1], (uint64_t)b[0]);
    divi = safe_divide((uint64_t)a[1], (uint64_t)b[0]) + safe_divide((rest << 32), (uint64_t)b[0]);
    holder[1] = (uint32_t)divi;
    rest = safe_rest((rest << 32) + (uint64_t)a[1], (uint64_t)b[0], divi);
    // rest = safe_rest((uint64_t)a[1], (uint64_t)b[0], divi) + safe_rest((rest << 32), (uint64_t)b[0], divi);

    // divi = safe_divide((rest << 32) + (uint64_t)a[0], (uint64_t)b[0]);
    divi = safe_divide((uint64_t)a[0], (uint64_t)b[0]) + safe_divide((rest << 32), (uint64_t)b[0]);
    holder[0] = (uint32_t)divi;

    add_u128(out, holder, out);
    reset_u128(holder);

    // divi = safe_divide((uint64_t)a[3], (uint64_t)b[1]);
    divi = safe_divide((uint64_t)a[3], (uint64_t)b[1]);
    holder[2] = (uint32_t)divi;
    rest = safe_rest((uint64_t)a[3], (uint64_t)b[1], divi);

    // divi = safe_divide((rest << 32) + (uint64_t)a[2], (uint64_t)b[1]);
    divi = safe_divide((uint64_t)a[2], (uint64_t)b[1]) + safe_divide((rest << 32), (uint64_t)b[1]);
    holder[1] = (uint32_t)divi;
    rest = safe_rest((rest << 32) + (uint64_t)a[2], (uint64_t)b[1], divi);

    // divi = safe_divide((rest << 32) + (uint64_t)a[1], (uint64_t)b[1]);
    divi = safe_divide((uint64_t)a[1], (uint64_t)b[1]) + safe_divide((rest << 32), (uint64_t)b[1]);
    holder[0] = (uint32_t)divi;

    add_u128(out, holder, out);
}
