from databricks import sql
import os


def querydb(a,b):
    query = "SELECT _c6 FROM default.applestore_csv WHERE _c5 = {0} AND _c0 = {1}".format(a, b)
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:
        
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result