"""
unesco_load.py
Loads date from csv and puts into django database: unesco
"""
import csv

from unesco.models import Category, State, Region, Iso, Site


def run():
    file_handler = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(file_handler)
    next(reader)  # advance past the header

    # Delete previous data
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    """
    csv format:
    name,description,justification,year,longitude,latitude,area_hectares,category,states,region,iso
    """

    for row in reader:
        try:
            category, __ = Category.objects.get_or_create(name=row[7])
        except IndexError:
            category = None
        try:
            state, __ = State.objects.get_or_create(name=row[8])
        except IndexError:
            state = None
        try:
            region, __ = Region.objects.get_or_create(name=row[9])
        except IndexError:
            region = None
        try:
            iso, __ = Iso.objects.get_or_create(name=row[10])
        except IndexError:
            iso = None
        try:
            name = row[0]
        except IndexError:
            name = None
        try:
            description = row[1]
        except IndexError:
            description = None
        try:
            justification = row[2]
        except IndexError:
            justification = None
        try:
            year = int(row[3])
        except ValueError:
            year = None
        try:
            longitude = float(row[4])
        except ValueError:
            longitude = None
        try:
            latitude = float(row[5])
        except ValueError:
            latitude = None
        try:
            area_hectares = float(row[6])
        except ValueError:
            area_hectares = None

        site = Site(
            name=name,
            description=description,
            justification=justification,
            year=year,
            longitude=longitude,
            latitude=latitude,
            area_hectares=area_hectares,
            category=category,
            state=state,
            region=region,
            iso=iso
        )
        site.save()
