// Prompts user for name and says hello using name

#include <stdio.h>
#include <cs50.h>

int main(void)
{
    str name = get_string("What's your name? ");
    printf("hello, %s\n", name);
}