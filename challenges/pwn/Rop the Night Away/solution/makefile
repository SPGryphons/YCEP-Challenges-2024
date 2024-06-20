X64       := gcc
CFLAGS    := -fno-stack-protector -no-pie
LIBC      := .
TARGET    := vuln
CHECKSEC  := checksec --file=$(TARGET)

all:
	$(X64) -o $(TARGET) *.c $(CFLAGS)

	@$(CHECKSEC)
aslr:
#	disable ASLR
	sudo bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'

clean:
	rm -f $(TARGET)

# export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH