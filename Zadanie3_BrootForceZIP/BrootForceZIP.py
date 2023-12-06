from tqdm import tqdm
import zipfile

wordlist = 'passwords.txt'
zip_file = 'test.zip'
zip_file = zipfile.ZipFile(zip_file)

n_words = len(list(open(wordlist,"rb")))

with open(wordlist,"rb") as wordlist:
    for word in tqdm(wordlist, total = n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("Пароль найден: ", word.decode().strip())
            exit(0)
print("Пароль не найден!")
