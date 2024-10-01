# fetch-reciept-analysis
 Reciepts data ETL and Analysis.


 ### File Structure
 ```
 fetch-reciept-analysis/
 ├─ config/                     - Contains config file for connecting to PostgreSQL
 ├─ data/                       - Contains raw json data as well as the SQL database dump after ETL
 ├─ src/                        - Contains complete ETL Pipeline. Can be run with 'python main.py'
 ├─ 1_Primary_Analysis.ipynb    - TASK1 :Primary Analysis to get the structure of data, used to form schema and perform ETL.
 ├─ 1_RelationalDataModel.png   - TASK1 : Relational Data Model schema diagram
 ├─ 2_queries.md                - TASK2 : Contains Queries and results from TASK 2
 ├─ 2_query_results/            - TASK2 : Contains Images of Query results of TASK 2
 ├─ 3_Data_Quality_Issues.ipynb - TASK3 : Deep dive into Data Quality Issues with SQL and Python
 ├─ 4_Email.md                  - TASK4 : Email for TASK 4
```

 ## Project Overview

 In this project, we analyze unstructured JSON data and design a new structured relational data model to meet business requirements. The project is broken down into several parts:

 - Data Model Design: Reviewing the provided data (Receipts, Users, and Brands) and designing a structured relational data model.
 - SQL Query Generation: Writing queries that answer specific business questions related to the data.
 - Data Quality Evaluation: Identifying potential data quality issues in the provided dataset.
 - Business Communication: Writing a message to communicate findings to a business stakeholder.

 ## ETL
 I developed an ETL pipeline located in the [ETL](/src) directory, which addresses minor data issues, extracts data from .gz files, removes duplicates, applies necessary mappings, and transforms the data to align with a newly designed Relational Data Model. The transformed data is then efficiently loaded into a PostgreSQL database.

 1. You can configure the connection to PostgreSQL by modifying the \config\config.json file.
 2. To execute the ETL process, simply run `python main.py` from the \src\ directory.

 ### Assumptions Made
 1. Name in the brands.json is the product name and not brand name. Each product has one barcode. each brandcode can have multiple barcodes. Therefore each row in brands corresponds to a different item and not a brand. This is evident from entries like 'Quaker Chewy' and 'Quaker Popped Crisps'
 2. barcode and brandcode of a receipt item corresponds with a item in brands database. There are inconsistencies with this rule aswell.
 3. Each User can have only one role at any given time.
 4. Barcode is unique per product. However this rule is violated in few places.
 5. Datafield types of certain datafields were assumed as show in the model schema below.

 ## Task 1: Review Existing Unstructured Data and Diagram a New Structured Relational Data Model /confif/config.json
 After examining the three JSON files provided thoroughly [Primary_Analysis](/1_Primary_Analysis.ipynb), I designed a structured relational model to efficiently store and query the data in a relational database. [Data_Model](/1_RelationalDataModel.png).



 ![Data_Model](/1_RelationalDataModel.png)

 ## Task 2: Write queries that directly answer predetermined questions from a business stakeholder

 I have written queries to answer all business problems [Queries](2_queries.md), I also ran this queries with minor adjustments to durations on the result of the ETL. Screenshots of results of PostgreSQL can be found in [Images](/2_query_results/)

 ## Task 3: Evaluate Data Quality Issues in the Data Provided

 I have used PostgreSQL and Python to dive deep and find data quality issues in the data provided. The highlights of the data issues and supporting code can be found in [Data_Quality_Issues](/3_Data_Quality_Issues.ipynb)


 ## Task 4: Communicate with Stakeholders

 I have drafted a email to talk to the Stakeholders requesting clarification, suggesting resolutions and talking about scaling the architecture. Please find it here [Email](/4_Email.md)



## Production Ready ETL Plan
 1. **Airflow, Dagster, or Prefect for Scheduling**
Use workflow orchestration tools like Airflow or Prefect to schedule ETL jobs, manage dependencies, and monitor execution, ensuring reliability and timely processing.

2. **dbt for Data Transformation**
Leverage dbt to automate data transformations, maintain version control, and validate models, ensuring consistency and data integrity across transformations.

3. **Databricks or Snowflake for OLAP**
Use Databricks or Snowflake to scale the pipeline, optimize performance, and handle large datasets with distributed computing and elastic storage.

4. **Tableau, Looker, or Power BI for Visualizations**
Create dashboards in Tableau, Looker, or Power BI, empowering users with real-time visual insights and interactive reports based on the transformed data.

5. **Alerts for DAG Failures and Performance**
Configure automated alerts via email or Slack for failed or slow DAGs, ensuring quick remediation to minimize disruptions and maintain ETL reliability.

6. **Comprehensive Logging**
Implement detailed logging of task execution, errors, and metadata to aid in auditing, troubleshooting, and performance tracking for smooth operations.

7. **Observability and Monitoring**
Use tools like Grafana or Datadog to monitor system health, resource utilization, and data freshness, enabling proactive optimization of the ETL pipeline.
