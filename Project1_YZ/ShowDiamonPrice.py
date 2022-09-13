from databricks import sql
import os


def querydb(carat=0.5, cut="Ideal", color="D", clarity="SI2"):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:
        query = "SELECT price FROM default.diamonds WHERE carat = {0} AND cut = {1} AND color = {2} AND clarity = {3}".format(carat, cut, color, clarity)
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result