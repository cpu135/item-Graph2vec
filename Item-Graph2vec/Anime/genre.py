import csv
genres={}
name={}
with open('../archive/anime_with_synopsis.csv') as fp1:
    f1_csv=csv.reader(fp1)
    headers=next(f1_csv)
    for row in f1_csv:
        genres[int(row[0])] = row[3]

with open('../archive/anime_with_synopsis.csv') as fp2:
    f2_csv=csv.reader(fp2)
    headers=next(f2_csv)
    for row in f2_csv:
        name[int(row[0])] = row[1]