from mod_python import apache

def index(req, zoekopdracht=""):
    req.content_type = 'text/html'
    req.write("<body bgcolor=yellow;>")
    req.write ("<b> Zoeken in de database: </b>")
    req.write("<form>")
    req.write("<Vul hier uw stof in: >")
    req.write("<input type = text name=zoekopdracht>")
    req.write("<input type = submit>")
    Zoekterm = zoeken_database(zoekopdracht)
    req.write("<zoekopdracht>")
    req.write("</form>")
    req.write("</body>")

def zoeken_database(zoekopdracht):
    "SELECT Journal, Pubmed_ID, Datum, Titel FROM Artikel"
    "WHERE Pubmed_ID = (SELECT artikel_pubmed_id"
    "FROM Relation_8 WHERE Stof_Stof_id = (SELECT Stof_id FROM Stof WHERE Naam = 'zoekopdracht'))"
    return zoekopdracht
