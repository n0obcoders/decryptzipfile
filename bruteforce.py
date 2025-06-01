from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False

def main():
    print("[+] Beginning brute-force attack...")

    try:
        with ZipFile('enc.zip') as zf: #you can add here your own file which you want to decrypt
            with open('rockyou.txt', 'rb') as f: #download rockyou password list or create your own through crunch
                for line in f:
                    password = line.strip()
                    if attempt_extract(zf, password):
                        print(f"[✔] Password found: {password.decode('utf-8')}")
                        return
                    else:
                        print(f"[-] Tried: {password.decode('utf-8')}")
    except FileNotFoundError:
        print("[!] enc.zip or rockyou.txt not found.")

    print("[✘] Password not found in list.")

if __name__ == "__main__":
    main()
