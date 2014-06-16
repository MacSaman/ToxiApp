## ---------------------------------------------------------------------------------------------------------------------------------
##    Auteur:       Teuntje Peeters Copyright 2014
##    Datum creatie: juni 2014
##    Versie:        1
##    Functionaliteit:
##    Bestand met stoffen doorlezen, opdelen in kolommen en de namen van de stoffen eruit halen en in een lijst plaatsten.
##    Connecteren met de mySQL connector database.
##    Dan zoekt deze pubmed door op zoek naar de stoffen uit het bestand en slaat deze op in de database.
##    Known bugs: 
## ---------------------------------------------------------------------------------------------------------------------------------

from Bio import Entrez
from Bio import Medline
import os
import mysql.connector

def main():
    Zoeken()

def Zoeken():
    try:
        conn = mysql.connector.connect(host = "127.0.0.1",
                                       user = "bi2_pg2",
                                       password = "blaat1234",
                                       db="bi2_pg2")
        print("Er is verbinding met de database")
        
        Entrez.email = 'A.N.Other@example.com'
        MAX_COUNT = 20
        Zoekwoord = raw_input("Vul hier uw stof in: ")
     
        h = Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=Zoekwoord)
        result = Entrez.read(h)
        print('Total number of publications containing {0}: {1}'.format(Zoekwoord, result['Count']))
        ids = result['IdList']

        h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
        records = Medline.parse(h)

        search_results = Entrez.read(Entrez.esearch(db="pubmed",
                                                term=Zoekwoord,
                                                reldate=365, datetype="pdat",
                                                usehistory="y"))

        count = int(search_results["Count"])

        cursor = conn.cursor ()
        authors = []
        for record in records:
            journal = record.get("TA", "?")
            datum = record.get("DA", "?")
            titel = record.get("TI", "?")
            abstract = record.get("AB", "?")
            Pubmed_ID = record.get("PMID", "?")

##            au = record.get('AU', '?')
##            for a in au: 
##                if a not in authors:
##                    authors.append(a)
##                authors.sort()
##                
            add_artikel = ("INSERT INTO Artikel"
                       "(Journal, Datum, Titel, Abstract, Pubmed_ID)"
                       "VALUES(%s, %s, %s, %s, %s)")
            
            data_artikel = (str(journal),str(datum),str(titel),str(abstract),str(Pubmed_ID))
##            data_auteurs = (str(au),str(au),str(pubmed_id))
            cursor.execute(add_artikel, data_artikel)
##            cursor.execute(add_auteurs, data_auteurs)
        conn.commit()
        cursor.close()
        conn.close()
        print("Artikel toevoegen is gelukt")

    except UnicodeEncodeError:
          print("UnicodeEncodeError")
