from datetime import date, datetime
import serial
import time
import urllib.request
import json
import csv
import smtplib

now = time.localtime(time.time())  # Obtenir l'heure et la date locale
year, month, day, hour, minute, second, weekday, yearday, daylight = now

secondsDiff = 3600 - (minute * 60)

Y = year  # dummy leap year to allow input X-02-29 (leap day)
seasons = [('hiver', (date(Y, 1, 1), date(Y, 3, 20))),
           ('printemps', (date(Y, 3, 21), date(Y, 6, 20))),
           ('ete', (date(Y, 6, 21), date(Y, 9, 22))),
           ('automne', (date(Y, 9, 23), date(Y, 12, 20))),
           ('hiver', (date(Y, 12, 21), date(Y, 12, 31)))]


def get_season(now):
    if isinstance(now, datetime):
        now = now.date()
    now = now.replace(year=Y)
    return next(season for season, (start, end) in seasons
                if start <= now <= end)


def get_angle():
    index = 0
    now = time.localtime(time.time())  # Obtenir l'heure et la date locale
    year, month, day, hour, minute, second, weekday, yearday, daylight = now

    if 0 >= hour < 4:
        index = 0
    elif 4 >= hour < 7:
        index = 1
    elif 7 >= hour < 10:
        index = 2
    elif 10 >= hour < 13:
        index = 3
    elif 13 >= hour < 16:
        index = 4
    elif 16 >= hour < 19:
        index = 5
    elif 19 >= hour < 22:
        index = 6
    elif 22 >= hour < 24:
        index = 7

    file = open("../donnees/%02d-%02d-%02d" % (year, month, day) + ".csv")
    content = file.readlines()
    list = content[index].split(",")
    maxvent = list[4]
    print("Le vent a une vitesse de ", maxvent)

    if int(maxvent) >= 16:
        arduino.write("0".encode())
        envoi_mail()
        print("Le vent est trop fort")
        print("Le panneau a un angle de 0°")
    else:
        if hour >= 7 and hour <= 20:
            print("C'est le jour. Le panneau est LIIIIIIIIIBBBBRRREEEEEEEEEEEEEEE")
            # ----- Hiver -----
            if hour == 7 and get_season(date.today()) == "hiver":
                arduino.write("0".encode())
                print("Le panneau a un angle de 0°")
            elif hour == 8 and get_season(date.today()) == "hiver":
                arduino.write("0".encode())
                print("Le panneau a un angle de 0°")
            elif hour == 9 and get_season(date.today()) == "hiver":
                arduino.write("35".encode())
                print("Le panneau a un angle de 35°")
            elif hour == 10 and get_season(date.today()) == "hiver":
                arduino.write("35".encode())
                print("Le panneau a un angle de 35°")
            elif hour == 11 and get_season(date.today()) == "hiver":
                arduino.write("30".encode())
                print("Le panneau a un angle de 30°")
            elif hour == 12 and get_season(date.today()) == "hiver":
                arduino.write("25".encode())
                print("Le panneau a un angle de 25°")
            elif hour == 13 and get_season(date.today()) == "hiver":
                arduino.write("25".encode())
                print("Le panneau a un angle de 25°")
            elif hour == 14 and get_season(date.today()) == "hiver":
                arduino.write("30".encode())
                print("Le panneau a un angle de 30°")
            elif hour == 15 and get_season(date.today()) == "hiver":
                arduino.write("30".encode())
                print("Le panneau a un angle de 30°")
            elif hour == 16 and get_season(date.today()) == "hiver":
                arduino.write("35".encode())
                print("Le panneau a un angle de 35°")
            elif hour == 17 and get_season(date.today()) == "hiver":
                arduino.write("0".encode())
                print("Le panneau a un angle de 0°")
            elif hour == 18 and get_season(date.today()) == "hiver":
                arduino.write("0".encode())
                print("Le panneau a un angle de 0°")
            elif hour == 19 and get_season(date.today()) == "hiver":
                arduino.write("0".encode())
                print("Le panneau a un angle de 0°")
            elif hour == 20 and get_season(date.today()) == "hiver":
                arduino.write("0".encode())
                print("Le panneau a un angle de 0°")

            # ----- Printemps -----
            elif hour == 7 and get_season(date.today()) == "printemps":
                arduino.write("0".encode())
                print("Le panneau a un angle de 0°")
            elif hour == 8 and get_season(date.today()) == "printemps":
                arduino.write("35".encode())
                print("Le panneau a un angle de 35°")
            elif hour == 9 and get_season(date.today()) == "printemps":
                arduino.write("30".encode())
                print("Le panneau a un angle de 30°")
            elif hour == 10 and get_season(date.today()) == "printemps":
                arduino.write("25".encode())
                print("Le panneau a un angle de 25°")
            elif hour == 11 and get_season(date.today()) == "printemps":
                arduino.write("20".encode())
                print("Le panneau a un angle de 20°")
            elif hour == 12 and get_season(date.today()) == "printemps":
                arduino.write("15".encode())
                print("Le panneau a un angle de 15°")
            elif hour == 13 and get_season(date.today()) == "printemps":
                arduino.write("15".encode())
                print("Le panneau a un angle de 15°")
            elif hour == 14 and get_season(date.today()) == "printemps":
                arduino.write("15".encode())
                print("Le panneau a un angle de 15°")
            elif hour == 15 and get_season(date.today()) == "printemps":
                arduino.write("20".encode())
                print("Le panneau a un angle de 20°")
            elif hour == 16 and get_season(date.today()) == "printemps":
                arduino.write("25".encode())
                print("Le panneau a un angle de 25°")
            elif hour == 17 and get_season(date.today()) == "printemps":
                arduino.write("30".encode())
                print("Le panneau a un angle de 30°")
            elif hour == 18 and get_season(date.today()) == "printemps":
                arduino.write("35".encode())
                print("Le panneau a un angle de 35°")
            elif hour == 19 and get_season(date.today()) == "printemps":
                arduino.write("0".encode())
                print("Le panneau a un angle de 0°")
            elif hour == 20 and get_season(date.today()) == "printemps":
                arduino.write("0".encode())
                print("Le panneau a un angle de 0°")

            # ----- Eté -----
            elif hour == 7 and get_season(date.today()) == "ete":
                arduino.write("35".encode())
                print("Le panneau a un angle de 35°")
            elif hour == 8 and get_season(date.today()) == "ete":
                arduino.write("30".encode())
                print("Le panneau a un angle de 30°")
            elif hour == 9 and get_season(date.today()) == "ete":
                arduino.write("25".encode())
                print("Le panneau a un angle de 25°")
            elif hour == 10 and get_season(date.today()) == "ete":
                arduino.write("20".encode())
                print("Le panneau a un angle de 20°")
            elif hour == 11 and get_season(date.today()) == "ete":
                arduino.write("15".encode())
                print("Le panneau a un angle de 15°")
            elif hour == 12 and get_season(date.today()) == "ete":
                arduino.write("15".encode())
                print("Le panneau a un angle de 15°")
            elif hour == 13 and get_season(date.today()) == "ete":
                arduino.write("15".encode())
                print("Le panneau a un angle de 15°")
            elif hour == 14 and get_season(date.today()) == "ete":
                arduino.write("15".encode())
                print("Le panneau a un angle de 15°")
            elif hour == 15 and get_season(date.today()) == "ete":
                arduino.write("15".encode())
                print("Le panneau a un angle de 15°")
            elif hour == 16 and get_season(date.today()) == "ete":
                arduino.write("15".encode())
                print("Le panneau a un angle de 15°")
            elif hour == 17 and get_season(date.today()) == "ete":
                arduino.write("20".encode())
                print("Le panneau a un angle de 20°")
            elif hour == 18 and get_season(date.today()) == "ete":
                arduino.write("25".encode())
                print("Le panneau a un angle de 25°")
            elif hour == 19 and get_season(date.today()) == "ete":
                arduino.write("30".encode())
                print("Le panneau a un angle de 30°")
            elif hour == 20 and get_season(date.today()) == "ete":
                arduino.write("35".encode())
                print("Le panneau a un angle de 35°")

            # ----- Automne -----
            elif hour == 7 and get_season(date.today()) == "automne":
                arduino.write("0".encode())
                print("Le panneau a un angle de 0°")
            elif hour == 8 and get_season(date.today()) == "automne":
                arduino.write("35".encode())
                print("Le panneau a un angle de 35°")
            elif hour == 9 and get_season(date.today()) == "automne":
                arduino.write("30".encode())
                print("Le panneau a un angle de 30°")
            elif hour == 10 and get_season(date.today()) == "automne":
                arduino.write("25".encode())
                print("Le panneau a un angle de 25°")
            elif hour == 11 and get_season(date.today()) == "automne":
                arduino.write("20".encode())
                print("Le panneau a un angle de 20°")
            elif hour == 12 and get_season(date.today()) == "automne":
                arduino.write("15".encode())
                print("Le panneau a un angle de 15°")
            elif hour == 13 and get_season(date.today()) == "automne":
                arduino.write("15".encode())
                print("Le panneau a un angle de 15°")
            elif hour == 14 and get_season(date.today()) == "automne":
                arduino.write("15".encode())
                print("Le panneau a un angle de 15°")
            elif hour == 15 and get_season(date.today()) == "automne":
                arduino.write("20".encode())
                print("Le panneau a un angle de 20°")
            elif hour == 16 and get_season(date.today()) == "automne":
                arduino.write("25".encode())
                print("Le panneau a un angle de 25°")
            elif hour == 17 and get_season(date.today()) == "automne":
                arduino.write("30".encode())
                print("Le panneau a un angle de 30°")
            elif hour == 18 and get_season(date.today()) == "automne":
                arduino.write("35".encode())
                print("Le panneau a un angle de 35°")
            elif hour == 19 and get_season(date.today()) == "automne":
                arduino.write("0".encode())
                print("Le panneau a un angle de 0°")
            elif hour == 20 and get_season(date.today()) == "automne":
                arduino.write("0".encode())
                print("Le panneau a un angle de 0°")
        else:
            arduino.write("0".encode())
            print("Le panneau est sécurisé pour la nuit")
            print("Le panneau a un angle de 0°")

def recup_meteo():
    url = "http://www.infoclimat.fr/public-api/gfs/json?_ll=46.70973,-2.35079&_auth=ARtUQwJ8UHIFKAQzAnQFLFgwVWAAdlVyB3tRMg9kB3oEYFczVjxTNgVpAXwALwIrBzZVKwg0VWgDYAtrWj5RLQF9VDICaFA0BW0EZAI2BTBYdFUqACJVbAd7USkPYwdjBGFXLVY0UzgFawF9ADICNAcqVT0IMlVyA38LbVoxUTMBY1Q3AmRQOwVvBGMCOwUuWHRVMwA%2FVWwHZVExDzQHNwRgVzRWPFM3BTwBYwAxAigHNlU8CD5VbANnC2haM1E1AX1ULwIYUEEFdwQmAnAFZFgtVSgAalUzBzA%3D&_c=464430debbb4ccd3f8e66a1132ab2e74"
    operUrl = urllib.request.urlopen(url)
    if (operUrl.getcode() == 200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
        exit()

    # Nettoyage du fichier
    del jsonData['request_state']
    del jsonData['request_key']
    del jsonData['message']
    del jsonData['model_run']
    del jsonData['source']

    fichier = open("../donnees/%02d-%02d-%02d" % (year, month, day) + ".csv", "w")

    for i, v in jsonData.items():
        print("{} --> {}, ".format(i, round(v['vent_rafales']['10m'] / 3.6)),
              " {},".format(round(v['vent_moyen']['10m'] / 3.6)), " {}".format(round(v['vent_direction']['10m'])))
        fichier.write("{},{},".format(i, round(v['vent_rafales']['10m'] / 3.6)) + "{},".format(
            round(v['vent_moyen']['10m'] / 3.6)) + "{}".format(round(v['vent_direction']['10m'])) + "\n")
    fichier.close()

def envoi_mail():
    serveur = smtplib.SMTP('smtp.gmail.com', 587)
    serveur.starttls()
    serveur.login('thibaultg78100@gmail.com', 'thibault1503')
    serveur.sendmail("thibaultg78100@gmail.com", "thibaultg78100@gmail.com", str("Bonjour Monsieur Bonvent \n Le vent sera fort aujourd'hui alors votre panneau sera securise. \n L'equipe de maintenance"))
    serveur.quit()

def recup_etat_panneau():
    if hour == 1 or hour == 4 or hour == 7 or hour == 10 or hour == 13 or hour == 16 or hour == 19 or hour == 22:
        serialArduino = serial.Serial('/dev/ttyACM0', 9600)
        line = serialArduino.readline().decode('utf-8').rstrip()
        data = line.split(',')

        fichier = open("../donnees/%02d-%02d-%02d" % (year, month, day) + "-etats.csv", "a")  # Ouvrir le fichier et écrire à la fin sans effacer le contenu précédent
        fichier.write(year + "," + month + "," + day + "," + hour + "," + data[0] + "\n")
        # data0 : état du panneau
        fichier.close()

def maj_date():
    now = time.localtime(time.time())  # Obtenir l'heure et la date locale
    year, month, day, hour, minute, second, weekday, yearday, daylight = now


with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
    if arduino.isOpen():
        print("{} est connecte!".format(arduino.port))
        arduino.write("0".encode())
        try:
            while True:
                print("Il est", hour, "h et nous sommes en", get_season(date.today()))
                now = time.localtime(time.time())  # Obtenir l'heure et la date locale
                year, month, day, hour, minute, second, weekday, yearday, daylight = now
                time.sleep(2)
                get_angle()
                recup_etat_panneau()
                time.sleep(secondsDiff)
                now = time.localtime(time.time())  # Obtenir l'heure et la date locale
                year, month, day, hour, minute, second, weekday, yearday, daylight = now

                if minute == 0:
                    now = time.localtime(time.time())  # Obtenir l'heure et la date locale
                    year, month, day, hour, minute, second, weekday, yearday, daylight = now
                    print("Il est", hour, "h et nous sommes en", get_season(date.today()))
                    now = time.localtime(time.time())  # Obtenir l'heure et la date locale
                    year, month, day, hour, minute, second, weekday, yearday, daylight = now
                    time.sleep(2)
                    get_angle()
                    recup_etat_panneau()
                    time.sleep(3600)
                    now = time.localtime(time.time())  # Obtenir l'heure et la date locale
                    year, month, day, hour, minute, second, weekday, yearday, daylight = now


                elif hour == 0:
                    now = time.localtime(time.time())  # Obtenir l'heure et la date locale
                    year, month, day, hour, minute, second, weekday, yearday, daylight = now
                    print("Un nouveau jour commence !!! Nous sommes le", day, month, year, "et nous sommes en", get_season(date.today()))
                    print("Il est", hour, "h et nous sommes en", get_season(date.today()))
                    now = time.localtime(time.time())  # Obtenir l'heure et la date locale
                    year, month, day, hour, minute, second, weekday, yearday, daylight = now
                    recup_meteo()
                    get_angle()
                    recup_etat_panneau()
                    time.sleep(3600)
                    now = time.localtime(time.time())  # Obtenir l'heure et la date locale
                    year, month, day, hour, minute, second, weekday, yearday, daylight = now


        except KeyboardInterrupt:
            print("Le programme a ete interrompu")
