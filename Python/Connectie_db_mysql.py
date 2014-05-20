import os
import mysql.connector


def main():
    Database();

def Database():
    conn = mysql.connector.connect(host = "http://cytosine.nl/phpmyadmin",
                                   user = "bi2_pg2",
                                   password = "blaat1234",
                                   db="owebi2_pg2")
    cursor = conn.cursor ()
    print("Er is verbinding met de database")

main()
