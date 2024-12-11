# Serverless API with AWS Lambda, API Gateway, and DynamoDB

## Overview
This project demonstrates how to build a serverless API using AWS Lambda, API Gateway, and DynamoDB. The API retrieves movie data stored in DynamoDB and returns it via a REST endpoint. This approach scales automatically and is cost-effective.

## Tech Stack
- Programming Language: Python
- AWS Services: Lambda, API Gateway, DynamoDB
- Tools: Boto3, Postman or curl

## Features
1. Data Storage: DynamoDB table for movie data
2. Serverless Compute: Lambda function to retrieve movie details
3. REST API: API Gateway to expose the Lambda function
4. Scalability: Automatically scales with traffic
5. Cost Efficiency: Pay only for what you use

## Architecture
- DynamoDB Table: Stores movie details keyed by `MovieID`
- Lambda Function: Fetches data from DynamoDB
- API Gateway: Provides a RESTful endpoint

## Prerequisites
- AWS account
- Python installed locally
- AWS CLI configured with proper credentials

## Steps
1. Create DynamoDB Table:  
   Run `python dynamodb/create_table.py` to create the DynamoDB table.
   
2. Deploy Lambda Function:
   - Navigate to the lambda folder: `cd lambda`
   - Zip the Lambda function: `zip function.zip lambda_function.py`
   - Upload `function.zip` to AWS Lambda using the AWS Management Console.
   - Configure the Lambda function with correct permissions and link it to the DynamoDB table.
   
3. Set Up API Gateway:
   - Open the AWS API Gateway Console.
   - Create a new REST API and add a `/movies` resource with a GET method.
   - Integrate the GET method with the Lambda function.
   - Deploy the API and note the endpoint URL.
   
4. Test the API:
   Use `curl "https://your-api-endpoint/movies?MovieID=1"` or Postman to test.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
