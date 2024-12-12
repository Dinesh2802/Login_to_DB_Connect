#import psycopg2

#connection = psycopg2.connect(
#    host = "localhost",
#   user = "postgres",
#   password = "Dinesh2802"
#)

#mediator = connection.cursor()

#mediator.execute("select version()")

#version_output = mediator.fetchone()

#print(version_output)

#-----------------------------------------
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
connection = psycopg2.connect(
     host = "localhost",
     user = "postgres",
     password = "Dinesh2802",
     database = "postgres"
 )

connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

mediator = connection.cursor()

mediator.execute("insert into sample(sno,name,age) values(1,'abc',20),(2,'xyz',21),(3,'pqr',22)")

connection.commit()

mediator.execute("select * from sample")

data = mediator.fetchall()

for i in data:
     print(i)

connection.close()
