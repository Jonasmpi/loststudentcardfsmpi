import smtplib
import sys
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# PythonScript für gefundene Studentenausweise
# Version 30.01.2017 / Python3

print("######################################################")
print(" \n   Emailclient für abgegebene Studentenausweise \n     Version 0.1 by Jonas Szalanczi    \n")
print("###################################################### \n")


def main():
    fromaddr = input("Deine FS-Emailadresselogin bitte eingeben: ")
    fromaddr = fromaddr + "@fsmpi.uni-bayreuth.de"
    print("Emails werden jetzt von " + fromaddr + " verschickt.....\n")
    text = (
    "Hallo, \ndein Studentenausweis wurde bei uns in der FS  Mathe Physik Informatik abgeben. \n Du kannst ihn gern während unserer Sprechstunden abholen.\n Unsere Sprechstunden sind Montag bis Donnerstag von 13-16 Uhr. Den Raum findest du neben dem H20. \n \n Viele Grüße \n Fachschaft Mathe Physik Informatik")
    subject = "Dein Studentenausweis abgegeben in der FS MPI"
    skennung = input("S-Kennung oder bt-Kennung des verlorenen Ausweises eingeben bitte: Bsp.( s1test ): \n")
    toaddr = (skennung + "@mail.uni-bayreuth.de")

    # Emailattribute....
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg.attach(MIMEText(text, 'plain'))

    messagetest = msg.as_string()
    print("Die Email wird an folgende Adresse geschickt " + toaddr)

    # Emailsendevorgang.....
    userinput = input("Wollen sie die Email senden (Y|N)")
    if userinput == "Y" or userinput == "y":
        server = smtplib.SMTP("STMPSERVER HIER", 587)
        server.starttls()
        userloginpw = getpass.getpass("Dein FS-EmailAccountPasswort: ")
        # Hacky Error/Authentification Handling...
        try:
            server.login(fromaddr, userloginpw)
            server.sendmail(fromaddr, toaddr, messagetest)
            server.quit
            print("Email wurde verschickt! \n Programm fertig.....")
        except:
            print("Login failed..neuer Versuch...... \n")
            main()
        exit()
    else:
        main()


main()