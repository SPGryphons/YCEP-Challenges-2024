#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>

char * get_flag() {
    int     fd;
    char *  flag;
    ssize_t read_bytes;

    if ( ( fd = open( "./flag.txt", O_RDONLY ) ) == -1 ) {
        printf( "couldn't open flag.txt file\n" );
        exit( 1 );
    }

    if ( ( flag = (char *)calloc( 0x50, sizeof( char ) ) ) == NULL ) {
        printf( "calloc failed\n" );
        close( fd );
        exit( 1 );
    }

    if ( ( read_bytes = read( fd, flag, 0x50 ) ) == -1 ) {
        printf( "couldn't read flag.txt file\n" );
        free( flag );
        close( fd );
        exit( 1 );
    }

    close( fd );
    return flag;
}

void slow_type( char * msg ) {
    /*
    thanks @Elma!
    */
    int i = 0;

    while ( 1 ) {
        if ( ! msg[i] ) {
            return;
        }

        putchar( msg[i] );
        usleep( 5000 );
        i += 1;
    }
}

void banner() {
    printf( "\n" );
    printf( "███████╗██╗███╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗ ██████╗ ███████╗    ██████╗  ██████╗ ██╗  ██╗   ██╗████████╗███████╗ ██████╗██╗  ██╗███╗   ██╗██╗ ██████╗\n" );
    printf( "██╔════╝██║████╗  ██║██╔════╝ ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗██║  ╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔════╝██║  ██║████╗  ██║██║██╔════╝\n" );
    printf( "███████╗██║██╔██╗ ██║██║  ███╗███████║██████╔╝██║   ██║██████╔╝█████╗      ██████╔╝██║   ██║██║   ╚████╔╝    ██║   █████╗  ██║     ███████║██╔██╗ ██║██║██║     \n" );
    printf( "╚════██║██║██║╚██╗██║██║   ██║██╔══██║██╔═══╝ ██║   ██║██╔══██╗██╔══╝      ██╔═══╝ ██║   ██║██║    ╚██╔╝     ██║   ██╔══╝  ██║     ██╔══██║██║╚██╗██║██║██║     \n" );
    printf( "███████║██║██║ ╚████║╚██████╔╝██║  ██║██║     ╚██████╔╝██║  ██║███████╗    ██║     ╚██████╔╝███████╗██║      ██║   ███████╗╚██████╗██║  ██║██║ ╚████║██║╚██████╗\n" );
    printf( "╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚══════╝╚═╝      ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝\n" );
    printf( "\n" );
}

void fake_entry() {

    /*
        This entire part is not relevant to the challenge ~~
    */

    char * line1 = "\e[1;33mBeginning application startup sequence...\n\e[0m";
    char * line2 = "\e[1;33mReading configuration from /etc/login.conf...\n\e[0m";
    slow_type( line1 );
    slow_type( line2 );
    sleep( 1 );

    char * line3 = "\e[1;32mFound authentication method, beginning login sequence...\n\n\e[0m";
    slow_type( line3 );

    printf( "Username: " );
    sleep( 1 );

    char * line4 = "gWBufFASOnLhNFRethHLpDeZVkAxdKCCuSiuuItogeDzTwlktC";
    slow_type( line4 );

    printf( "\n" );
    printf( "Password: " );

    sleep( 1 );
    char * line5 = "ed36f2e156df486fcc9e5ff854f47fd9f67c2bcbfcfa30fccb36f72dca22a81799baee504a1fe91a07bc66b6900bd39874191889";
    slow_type( line5 );
    printf( "\n" );

    sleep( 1 );

    printf( "\n" );
    char * line6 = "\e[1;32mSuccessfully logged in, redirecting... \n\e[0m";
    slow_type( line6 );

    char * line7 = "\e[1;33m[*] 2FA is enabled for this account, please check your authenticator device for the code. \n\e[0m";
    slow_type( line7 );
    printf( "\n" );
}

void dashboard() {
    char * flag  = get_flag();
    char * line1 = "\n\e[1;32mLogin successful, spawning a shell...\n\e[0m";
    slow_type( line1 );
    sleep( 1 );

    printf( "\nroot@gryphons:~# " );
    sleep( 1 );

    char * line2 = "ls\n";
    slow_type( line2 );

    sleep( 1 );

    char * line3 = "flag.txt   run\n\n";
    slow_type( line3 );

    printf( "root@gryphons:~# " );
    sleep( 2 );

    char * line4 = "cat flag.txt\n";
    slow_type( line4 );

    printf( "\e[1;33m%s\e[0m\n\n", flag );

    printf( "root@gryphons:~# " );
    sleep( 1 );
    char * line5 = "exit\n";

    slow_type( line5 );

    free( flag );
    exit( 0 );
}

int main( int argc, char * argv[] ) {

    setbuf( stdin, 0 );
    setbuf( stdout, 0 );

    char otp[0x50]    = { 0 };
    int  is_otp_valid = 0xcafebabe;

    banner();
    fake_entry();
    printf( ">> " );

    fgets( otp, 100, stdin );

    /*
        TODO: Implement OTP validation, we'll just classify OTP as not implemented for now.
    */

    if ( is_otp_valid == 0xdeadbeef ) {
        dashboard();
    } else {
        printf( "\e[1;31mOTP support not implemented yet, sorry!~\n\e[0m" );
    }

    return 0;
}