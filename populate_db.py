import csv
import os
from random import randint
from core.shortener import Shortener
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    execute_from_command_line(["manage.py", "flush"])
    with open("top500Domains.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            url = row[1]
            visits = randint(1000, 100000)
            shortener = Shortener(url)
            shortener.shorten_url()
            shortener.url_object.visits = visits
            shortener.url_object.save()
