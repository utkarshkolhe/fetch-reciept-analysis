
**Subject:** Data Quality and Optimization Concerns for Transactions Data

Hi Good Morning,

Hope you're doing well! I wanted to share some insights and raise a few questions regarding the transactions data that you have provided.

I identified some data quality issues through thorough data profiling, analyzing missing values and duplicates, validating categorical values, and performing joins across tables to reveal inconsistencies in Users, Brands and Receipts data:
1. The data has huge amounts of duplicates, particularly of users. This level of duplication would result in inaccurate updates and storage wastage if left unchecked.
2. Many records of users, brands and barcodes are missing in the data even though some receipts reference them. This could be a major design flaw in data capture.
3. Key data fields like barcode, categories and barcodes are either missing or inconsistent leading to issues in joining data.  

Here are few things which would help me resolve this issues:
-   Understanding how brand, barcode, and user data is currently captured can help me identify the root cause of missing or incorrect data.
- Are there any backups or replicas of the databases?
-   How should we handle cases where barcodes correspond to multiple brands? Are there any guidelines on how barcodes are used in the system?


Performance Concerns:

With the current data inconsistencies, scaling this to production could lead to significant inaccuracies in mapping receipts to brands and users. To address this, I recommend establishing a validation layer during data ingestion to detect and resolve inconsistencies before they affect downstream systems.

As our dataset grows, I anticipate query performance issues. I plan to implement indexing, partitioning, and caching strategies to maintain scalability.

I would appreciate your thoughts and any additional context that may help resolve these issues more effectively. Please let me know if you’d like to discuss this further or require a more detailed breakdown of the issues.

Regards,  
Utkarsh Kolhe
