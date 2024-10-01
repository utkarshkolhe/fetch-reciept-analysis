# Queries


## Q1) What are the top 5 brands by receipts scanned for most recent month?
Question is bit unclear about how many times a receipts should be counted if one receipt has multiple items form same brand. I assumed it to be counted with respect to items and not once per receipt.

```sql

WITH RecentMonthReceipts AS (
  -- Find receipts from the most recent month
  SELECT *
  FROM Receipts
  WHERE dateScanned >= (SELECT DATE_TRUNC('month', MAX(dateScanned)) FROM Receipts)
)
SELECT
  RANK() OVER (ORDER BY COUNT(ri._id) DESC) AS brandRank,
  b.name AS brandName,
  COUNT(ri._id) AS receiptCount
FROM ReceiptItems ri
JOIN RecentMonthReceipts r ON ri.recieptID = r._id
JOIN Brands b ON ri.brandID = b._id
GROUP BY b.name
ORDER BY brandRank
LIMIT 5;

```
Result on quering on the data. Instead of using most recent month '2021-01-01' was used since it is the only month with good data in the dataset.<br>
![Q1](https://github.com/utkarshkolhe/fetch-reciept-analysis/blob/main/query_results/Q1.jpg)

##  Q2) How does the ranking of the top 5 brands by receipts scanned for the recent month compare to the ranking for the previous month?
```sql
WITH RecentMonthReceipts AS (
  -- Find receipts from the most recent month
  SELECT *
  FROM Receipts
  WHERE dateScanned >= (SELECT DATE_TRUNC('month', MAX(dateScanned)) FROM Receipts)
),
SecondRecentMonthReceipts AS (
  -- Find receipts from the second most recent month
  SELECT *
  FROM Receipts
  WHERE dateScanned >= (SELECT DATE_TRUNC('month', MAX(dateScanned)) - INTERVAL '1 month'FROM Receipts)
 		AND dateScanned < (SELECT DATE_TRUNC('month', MAX(dateScanned)) FROM Receipts)
),
RecentMonthBrandRanks AS (
  -- Rank brands based on the most recent month
  SELECT
    b.name AS brandName,
    COUNT(ri._id) AS receiptCount,
    RANK() OVER (ORDER BY COUNT(ri._id) DESC) AS brandRank
  FROM ReceiptItems ri
  JOIN RecentMonthReceipts r ON ri.recieptID = r._id
  JOIN Brands b ON ri.brandID = b._id
  GROUP BY b.name
),
SecondRecentMonthBrandRanks AS (
  -- Rank brands based on the second most recent month
  SELECT
    b.name AS brandName,
    COUNT(ri._id) AS receiptCount,
    RANK() OVER (ORDER BY COUNT(ri._id) DESC) AS brandRank
  FROM ReceiptItems ri
  JOIN SecondRecentMonthReceipts r ON ri.recieptID = r._id
  JOIN Brands b ON ri.brandID = b._id
  GROUP BY b.name
)
SELECT
  COALESCE(rm.brandName, sm.brandName) AS brandName,
  rm.brandRank AS mostRecentRank,
  sm.brandRank AS secondMostRecentRank,
  COALESCE(sm.brandRank, 0) - COALESCE(rm.brandRank, 0) AS rankChange
FROM SecondRecentMonthBrandRanks sm
FULL OUTER JOIN RecentMonthBrandRanks rm
ON sm.brandName = rm.brandName
ORDER BY mostRecentRank ASC
LIMIT 5;

```
Result on quering on the data. Instead of using most recent month and second most recent month both months were taken as '2021-01-01' used since it is the only month with good data in the dataset.<br>
![Q2](https://github.com/utkarshkolhe/fetch-reciept-analysis/blob/main/query_results/Q2.jpg)

## Q3) When considering average spend from receipts with 'rewardsReceiptStatus' of 'Accepted' or 'Rejected', which is greater?

 Since data did not have "ACCEPTED" rewardsReceiptStatus, I assumed they meant "FINISHED".
All Unique  rewardsReceiptStatus in the data are "REJECTED", "SUBMITTED", "FLAGGED", "PENDING", "FINISHED"

```sql
SELECT
  rewardsReceiptStatus,
  AVG(totalSpent) AS averageSpend
FROM Receipts
WHERE rewardsReceiptStatus IN ('FINISHED', 'REJECTED')
GROUP BY rewardsReceiptStatus
ORDER BY averageSpend DESC;
```
Result on quering on the data.<br>
![Q3](https://github.com/utkarshkolhe/fetch-reciept-analysis/blob/main/query_results/Q3.jpg)



## Q4) When considering  _total number of items purchased_  from receipts with 'rewardsReceiptStatus’ of ‘Accepted’ or ‘Rejected’, which is greater?

 Same as Q3, since data did not have "ACCEPTED" rewardsReceiptStatus, I assumed they meant "FINISHED".
All Unique  rewardsReceiptStatus in the data are "REJECTED", "SUBMITTED", "FLAGGED", "PENDING", "FINISHED"

```sql
SELECT
  r.rewardsReceiptStatus,
  SUM(ri.quantityPurchased) AS totalItemsPurchased
FROM Receipts r
JOIN ReceiptItems ri ON r._id = ri.recieptID
WHERE r.rewardsReceiptStatus IN ('FINISHED', 'REJECTED')
GROUP BY r.rewardsReceiptStatus
ORDER BY totalItemsPurchased DESC;
```
Result on quering on the data.<br>
![Q4](https://github.com/utkarshkolhe/fetch-reciept-analysis/blob/main/query_results/Q4.jpg)


## Q5) Which brand has the most  _spend_  among users who were created within the past 6 months?


```sql
SELECT
  b.name AS brandName,
  SUM(ri.finalPrice) AS totalSpend
FROM Users u
JOIN Receipts r ON u._id = r.userId
JOIN ReceiptItems ri ON r._id = ri.recieptID
JOIN Brands b ON ri.brandID = b._id
WHERE u.createdDate >= NOW() - INTERVAL '6 months'
GROUP BY b.name
ORDER BY totalSpend DESC
LIMIT 1;
```
Result on quering on the data. Instead of using last 6 months all of the users were used since the data does not have 6 months data.<br>
![Q5](https://github.com/utkarshkolhe/fetch-reciept-analysis/blob/main/query_results/Q5.jpg)


## Q6) Which brand has the most  _transactions_  among users who were created within the past 6 months?
In this case transaction is considered once per brand on a receipt, even if you purchased multiple items from the same brand on that receipt because payment is done only once per receipt.

```sql
SELECT
  b.name AS brandName,
  COUNT(distinct r._id) AS transactionCount
FROM Users u
JOIN Receipts r ON u._id = r.userId
JOIN ReceiptItems ri ON r._id = ri.recieptID
JOIN Brands b ON ri.brandID = b._id
WHERE u.createdDate >= NOW() - INTERVAL '6 months'
GROUP BY b.name
ORDER BY transactionCount DESC
LIMIT 1;
```
Result on quering on the data. Instead of using last 6 months all of the users were used since the data does not have 6 months data.<br>
![Q6](https://github.com/utkarshkolhe/fetch-reciept-analysis/blob/main/query_results/Q6.jpg)
