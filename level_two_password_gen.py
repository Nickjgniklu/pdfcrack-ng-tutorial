import io
month_days= [31,29,31,30,31,30,31,31,30,31,30,31]
with io.open("level_two_passwords.txt", "w", encoding="ISO-8859-1") as outputFile:
    for year in range(1900,2022):
        for month in range(12):
            for day in range(month_days[month]):
                outputFile.write(f'{year}:{month+1:02d}:{day+1:02d}\n')
