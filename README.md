Serverless API with AWS Lambda, API Gateway, and DynamoDB

Project Overview

This project demonstrates how to build a serverless API using AWS services such as Lambda, API Gateway, and DynamoDB. The API retrieves movie information stored in a DynamoDB table and provides it via a RESTful endpoint. This architecture leverages the scalability and cost-effectiveness of serverless computing.

Tech Stack

Programming Language: Python

AWS Services:

AWS Lambda (compute)

Amazon API Gateway (API management)

Amazon DynamoDB (data storage)

Tools:

Boto3 (AWS SDK for Python)

Postman or curl (for API testing)

Features

Data Storage: Store movie data in a DynamoDB table.

Serverless Compute: AWS Lambda function to retrieve movie details.

REST API: API Gateway setup to expose the Lambda function.

Scalability: Automatically scales with traffic.

Cost Efficiency: Pay only for the resources used.

Architecture

The serverless architecture includes:

DynamoDB Table: Stores movie details with MovieID as the primary key.

Lambda Function: Handles API requests and fetches data from DynamoDB.

API Gateway: Provides a RESTful endpoint to access the Lambda function.

Setup Instructions

Prerequisites

AWS account

Python installed on your local machine

AWS CLI configured with proper credentials

Steps

Clone this Repository:

git clone https://github.com/your-username/serverless-api-aws.git
cd serverless-api-aws

Create DynamoDB Table:
Run the provided script to create a DynamoDB table:

python dynamodb/create_table.py

Deploy Lambda Function:

Zip the Lambda function:

cd lambda
zip function.zip lambda_function.py

Upload the zip to AWS Lambda and configure the function to connect with your DynamoDB table.

Setup API Gateway:

Create a REST API in API Gateway.

Add a GET method linked to your Lambda function.

Deploy the API and note the endpoint URL.

Test the API:
Use Postman or curl to send a GET request to the endpoint:

curl -X GET "https://your-api-endpoint/movies?MovieID=1"

Example Request

curl -X GET "https://your-api-endpoint/movies?MovieID=1"

Example Response

{
  "MovieID": "1",
  "Title": "Inception",
  "Director": "Christopher Nolan",
  "Year": "2010"
}

Project Structure

serverless-api-aws/
├── README.md                # Project documentation
├── lambda/
│   ├── lambda_function.py   # Lambda function code
├── dynamodb/
│   ├── create_table.py      # Script to create DynamoDB table
├── requirements.txt         # Python dependencies
└── .gitignore               # Files to ignore in version control

Key Benefits of Serverless Architecture

No Server Management: AWS handles infrastructure for you.

Automatic Scaling: Scales based on traffic.

Cost Efficiency: Pay only for what you use.

Contributing

Contributions are welcome! If you find any issues or have suggestions, feel free to open a pull request or create an issue.
