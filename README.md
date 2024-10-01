# fetch-reciept-analysis
 Reciepts data ETL and Analysis.


 ### File Structure
 ```
 fetch-receipt-processor/
 ├─ config/                     - Contains config file for connecting to PostgreSQL
 ├─ data/                       - Contains raw json data as well as the SQL database after ETL
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

 ## Task 1: Review Existing Unstructured Data and Diagram a New Structured Relational Data Model

 After examining the three JSON files provided thoroughly [Primary_Analysis](/1_Primary_Analysis.ipynb), I designed a structured relational model to efficiently store and query the data in a relational database. [Data_Model](/1_RelationalDataModel.png).

 I also wrote a ETL code in [ETL](/src/) which perform minor data issue fixes and loads data on PostgreSQL.

 ![Data_Model](/1_RelationalDataModel.png)

 ## Task 2: Write queries that directly answer predetermined questions from a business stakeholder

 I have written queries to answer all business problems [Queries](2_queries.md), I also ran this queries with minor adjustments to durations on the result of the ETL. Screenshots of results of PostgreSQL can be found in [Images](/2_query_results/)

 ## Task 3: Evaluate Data Quality Issues in the Data Provided

 I have used PostgreSQL and Python to dive deep and find data quality issues in the data provided. The highlights of the data issues and supporting code can be found in [Data_Quality_Issues](/3_Data_Quality_Issues.ipynb)


 ## Task 4: Communicate with Stakeholders

 I have drafted a email to talk to the Stakeholders requesting clarification, suggesting resolutions and talking about scaling the architecture. Please find it here [Email](/4_Email.md)
