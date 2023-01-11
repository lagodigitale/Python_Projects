import psycopg2

# Variable de connection à la base de donnée
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '2002'
DATABASE = 'cahier'

# Connection au serveur

try:
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD)
    print("conection reussie!!")
except psycopg2.Error as e:
    print("connection refusé veillez verifir les paramettre de connection!!")

    # Validation des transaction

connection.autocommit = True
cursor = connection.cursor()

# Creation de la BD
cursor.execute('DROP DATABASE IF EXISTS {};'.format('cahier_dentree'))
cursor.execute("CREATE DATABASE cahier_dentree;")

#Creation de la table student

#cursor.execute("CREATE TABLE entrants (name VARCHAR(255), firstname VARCHAR(255), phone VARCHAR(255), cnib VARCHAR(255));")

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Task(models.Model):
    content = models.CharField(_(u'task'), max_length=255)
    is_resolved = models.BooleanField(_(u'Resolved?'))

    def __unicode__(self):
        return u'Task %d : %s' % (self.id, self.content)
