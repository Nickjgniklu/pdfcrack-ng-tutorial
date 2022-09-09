import io
with io.open("level_one_passwords.txt", "w", encoding="ISO-8859-1") as outputFile:
    for i in range(2000):
        outputFile.write(f'password{i}\n')