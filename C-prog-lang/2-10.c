/* Exercise 2-10. Rewrite the function `lower`, which converts upper case
 * letters to lower casse, with a conditional expression intead of
 * `if-else`.
 */

#include <stdio.h>

char lower(char c);

int main(void)
{
    char s[12] = "hElLO, WorLD";
    printf("s: %s\n", s);

    printf("lowercase s: ");
    for (int i=0; i<12; i++)
        putchar(lower(s[i]));
    putchar('\n');

    return 0;
}

char lower(char c)
{
    return (c>='A' && c<='Z') ? c+('a'-'A') : c;
}
