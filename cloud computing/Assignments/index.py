import boto3
from time import sleep
import mysql.connector
import textwrap

client = boto3.client('rds')

DBNAME='database1'
ALLOCATED=20
SGGROUP=''
ENGINE='mysql'
PORT=3306
MASTERUSER='admin'
MASTERPASSWORD='admin123'

def create_db():
    response = client.create_db_instance(
        DBName=DBNAME,
        DBInstanceIdentifier=DBNAME,
        AllocatedStorage=ALLOCATED,
        DBInstanceClass='db.t2.micro',
        Engine=ENGINE,
        MasterUsername=MASTERUSER,
        MasterUserPassword=MASTERPASSWORD,
        VpcSecurityGroupIds=[
            SGGROUP,
        ],
        Port=PORT,
        PubliclyAccessible=True)

    print("Started creation")

def get_db_endpoint():
    response = client.describe_db_instances(
        DBInstanceIdentifier=DBNAME
    )
    endpoint = response['DBInstances'][0]['Endpoint']['Address']
    print("Endpoint is: ", endpoint)
    return endpoint

def create_database_model():
    endpoint = get_db_endpoint()
    host_args = {
        "host": endpoint,
        "user": MASTERUSER,
        "password": MASTERPASSWORD
    }

    con = mysql.connector.connect(**host_args)

    cur = con.cursor(dictionary=True)
    
    print("Starting modelling")
    with open('queries.sql', 'r') as sql_file:
        result_iterator = cur.execute(sql_file.read(), multi=True)
        for res in result_iterator:
            print("Running query: ", res)  # Will print out a short representation of the query
            print(f"Affected {res.rowcount} rows" )

    print("Successful execution")

create_db()
sleep(600)
create_database_model()
