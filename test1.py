import csv
from os import spawnlp

with open('./csv_file', 'w') as f:
    print("opened a file")
    spamwriter = csv.writer(f, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    for x in range(2, 17):
        spamwriter.writerow(['https://usa.businessdirectory.cc/philadelphia/ads'])