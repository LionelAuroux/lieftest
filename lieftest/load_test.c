#include <unistd.h>
#include <alloca.h>
#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>

void    my_log(const char *fmt, ...)
{
    va_list ap;

    va_start(ap, fmt);
    size_t sz = vsnprintf(NULL, 0, fmt, ap);
    va_end(ap);
    char *buf = alloca(sz + 2);
    va_start(ap, fmt);
    vsnprintf(buf, sz + 1, fmt, ap);
    va_end(ap);
    write(2, buf, sz);
}

int main()
{
    unsigned char    buf[64];
    if (isatty(0))
    {
        my_log("ISATTY TRUE\n");
        exit(1);
    }
    read(0, buf, 64);
    
    my_log("LOADING!\n");

    for (int i = 0; i < 64; i += 1)
    {
        my_log("%02X ", buf[i]);
    }
    my_log("\n");
}
