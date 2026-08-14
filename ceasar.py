mkdir caesar-cipher && cd caesar-cipher && cat << 'EOF' > caesar.py
import sys

def caesar(text, shift, mode):
    result = ""
    shift = shift if mode == 'e' else -shift
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

if len(sys.argv) < 4:
    print("Usage: python3 caesar.py <e|d> <shift_number> \"text\"")
    sys.exit(1)

print(caesar(sys.argv[3], int(sys.argv[2]), sys.argv[1]))
EOF
