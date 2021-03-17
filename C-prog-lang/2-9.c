/* Exercise 2-9. In a two's complement number system, `x &= (x-1)`
 * deletes the rightmost 1-bit in `x`. Explain why. Use this observation
 * to write a faster version of `bitcount`.
 */

#include <stdio.h>

int bitcount(unsigned x);
int bitcount_new(unsigned x);

int main(void)
{
    unsigned x = 31;
    printf("x = %u, bitcount(x) = %d, bitcount_new(x) = %d\n",
            x, bitcount(x), bitcount_new(x));

    x = 32;
    printf("x = %u, bitcount(x) = %d, bitcount_new(x) = %d\n",
            x, bitcount(x), bitcount_new(x));

    x = 731;
    printf("x = %u, bitcount(x) = %d, bitcount_new(x) = %d\n",
            x, bitcount(x), bitcount_new(x));
    return 0;
}

// bitcount: count 1 bits in x
int bitcount(unsigned x)
{
    int b;
    for (b = 0; x != 0; x >>= 1)
        if (x & 01)
            b++;
    return b;
}

int bitcount_new(unsigned x)
{
    int b;
    for (b = 0; x != 0; x &= (x-1))
        b++;
    return b;
}
