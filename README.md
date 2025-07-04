CODTECH Internship – Task 1

Task Title:
Big Data Analysis Using Scalable Tools (Dask)

Objective:
Analyze a large dataset (Amazon Fashion reviews) using Dask to demonstrate scalable data processing without needing Hadoop or Spark on Windows.

Dataset Used:
Name: AMAZON_FASHION.csv
Records: ~883,636 reviews
Source: Provided/intern's dataset

Tools & Technologies:
Python 3.10
Dask
Pandas
PyCharm (IDE)

Steps Performed:
1. Loaded large CSV file using Dask
2. Displayed top 5 records
3. Counted total number of rows
4. Verified vs Unverified review counts
5. Calculated average product rating

Sample Output (Console):
Top 5 Rows:
overall verified reviewTime ... style image
0 5.0 True 10 20, 2014 ... <NA> <NA>

Total Rows: 883636

Verified/Unverified Review Count:
verified
False 125630
True 758006
dtype: int64

Average Overall Rating: 4.21


File Structure:
📁 Task-1/
├── t1.py
├── AMAZON_FASHION.csv (optional sample or full)
└── README.md


Intern Info:
Name: Kapil Lakhchaura
Course: BCA, 5th Semester
University: Uttaranchal University
Internship Provider: CODTECH IT Solutions Pvt. Ltd.
