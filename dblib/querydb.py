import os
from databricks import sql

def querydb(income=50):
    query = "SELECT Spending_Score FROM default.mallcustomers_csv WHERE Annual_Income = {0}".format(
        income
    )
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
