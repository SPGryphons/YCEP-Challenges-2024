X64       := /usr/bin/x86_64-linux-gnu-gcc
CFLAGS    := -fno-stack-protector
TARGET    := vuln
CHECKSEC  := checksec --file=$(TARGET)

all:
	$(X64) -o $(TARGET) *.c $(CFLAGS)
	@#/usr/bin/x86_64-linux-gnu-gcc -o vuln *.c

	@$(CHECKSEC)

aslr:
#	disable ASLR
	sudo bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'

clean:
	rm -f $(TARGET)