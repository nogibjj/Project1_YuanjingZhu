# Project1_YuanjingZhu_QueryCustomerSpendingScore

[![Python application test with Github Actions](https://github.com/nogibjj/nogibjj-IDS706_Project1_YZ/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/nogibjj-IDS706_Project1_YZ/actions/workflows/main.yml)

This the repository for project 1 of IDS706Data_Engineering_Systemm

## Overview
In this project, I downloaded a Mall Customer Segmentation Dataset from Kaggle and upload to the Databricks. Then I connect my Github Codespaces with my Databricks cluster, wrote a function to excute SQL query, built a command line tool and finally a simple web app. By default, the query returns the spending score of customers with $50k annual income, and users can put any income number they are interested in and all the customers' spending score will be displayed. 



## Dataset
The dataset comes from [Kaggle](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python). It contains customer information including Customer ID, age, gender, annual income and spending score from a supermarket. The spending score is assigned to each customer based on their spending nature and purchasing behavior. By analyzing the dataset, the supermarket owner can segment their customers and excute effective strategy accordingly. 

<img src="https://user-images.githubusercontent.com/110933007/190728414-a6779a6d-a885-4867-bc88-953b0170ae64.png" >



## Connecting Codespaces and Databricks

Created four secrets in GitHub settings. The four secrets are DATABRICKS_HOST, DATABRICKS_HTTP_PATH, DATABRICKS_SERVER_HOSTNAME and DATABRICKS_TOKEN.

<img src="https://user-images.githubusercontent.com/110933007/190536619-6dec85d9-e301-461c-8e13-f248101f72ca.png" width=75% height=75%>

Then test the following code in Codespaces to check the connection. 

```
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq
```

## SQL query

The default sql query will return the spending score of customers whose annual income are $50,000. Using the querydb function, it will return the spending score of all customers whose annual income is the number assigned. \
For example:

<img src="https://user-images.githubusercontent.com/110933007/190535012-62bccc33-f80a-442d-b320-6819ca1c9a76.png" width=85% height=85%>


## Command line tool
```
chmod +x query_mall_sql_db.py 
./query_mall_sql_db.py cli-query  --help
./query_mall_sql_db.py cli-query  --income "60"
```
The ```chmod``` command is used to manage file system access permissions on Unix and Unix-like systems, ```+x``` means to excute.  ```chi-query``` is the function name. Type ```--help``` to see the instruction or type ```--income"int"``` to excute the sql query. 

## Web app
```
python fastapi-app.py 
```
After typing the code in the terminal, a new web page will open and the home page says "Welcome to my Databricks sql query!". Type "/query" at the end of the url, the web page will return the customer's spending score. 

<img src="https://user-images.githubusercontent.com/110933007/190729294-efa7d319-a915-49db-bd44-0c28600aaa61.png" width=60% height=60%>


