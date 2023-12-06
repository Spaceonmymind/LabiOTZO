import pikepdf
from tqdm import tqdm

passwords = [line.strip() for line in open("passwords.txt", encoding = 'UTF-8')]

for password in tqdm(passwords, "Расшифровка PDF-файла"):
    try:
        with pikepdf.open("pdfTest.pdf", password=password) as pdf:
            print("Пароль найден: ", password)
            break
    except pikepdf._qpdf.PasswordError:
        continue