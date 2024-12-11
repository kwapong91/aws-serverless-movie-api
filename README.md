# **Serverless API with AWS Lambda, API Gateway, and DynamoDB**

## **Project Overview**  
This project demonstrates how to build a serverless API using AWS services such as **Lambda**, **API Gateway**, and **DynamoDB**. The API retrieves movie information stored in a DynamoDB table and provides it via a RESTful endpoint. This architecture leverages the scalability and cost-effectiveness of serverless computing.

---

## **Tech Stack**  
- **Programming Language:** Python  
- **AWS Services:**  
  - AWS Lambda (compute)  
  - Amazon API Gateway (API management)  
  - Amazon DynamoDB (data storage)  
- **Tools:**  
  - Boto3 (AWS SDK for Python)  
  - Postman or curl (for API testing)  

---

## **Features**  
1. **Data Storage:** Store movie data in a DynamoDB table.  
2. **Serverless Compute:** AWS Lambda function to retrieve movie details.  
3. **REST API:** API Gateway setup to expose the Lambda function.  
4. **Scalability:** Automatically scales with traffic.  
5. **Cost Efficiency:** Pay only for the resources used.  

---

## **Architecture**  
The serverless architecture includes:  
- **DynamoDB Table:** Stores movie details with `MovieID` as the primary key.  
- **Lambda Function:** Handles API requests and fetches data from DynamoDB.  
- **API Gateway:** Provides a RESTful endpoint to access the Lambda function.  

---

## **Setup Instructions**

### **Prerequisites**  
- AWS account  
- Python installed on your local machine  
- AWS CLI configured with proper credentials  

### **Steps**  
1. **Clone this Repository:**  
   ```bash
   git clone https://github.com/your-username/serverless-api-aws.git
   cd serverless-api-aws
