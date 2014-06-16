from Bio import Entrez
from Bio import Medline
import os
import mysql.connector

def main():
    bestand_lezen()
##    stof_invoeren()

def bestand_lezen():
    counter = 0
    nieuwe_lijst = []
    bestand = open("Stoffenlijst.txt").readlines()
    for line in bestand:
        regel = line.split("\t")
        lijst = [regel[0].lower()]
        for i in lijst:
            if i not in nieuwe_lijst:
                nieuwe_lijst.append(i)
    for i in nieuwe_lijst:
        counter +=1
        stof_invoeren(i, counter)

def stof_invoeren(stof, counter):    
    conn = mysql.connector.connect(host = "127.0.0.1",
                                       user = "bi2_pg2",
                                       password = "blaat1234",
                                       db="bi2_pg2")
    cursor = conn.cursor ()
    
    add_stof = ("INSERT INTO Stof"
                       "(Stof_id, Naam)"
                       "VALUES(%s, %s)")

    data_stof = (str(counter),str(stof))
    cursor.execute(add_stof, data_stof)
    conn.commit()
        
    cursor.close()
    conn.close()
    print("Stof ingevoerd")

main()
