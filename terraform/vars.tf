# Define the AWS region variable
variable "AWS_REGION" {
  description = "The AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

# Define the database password variable
variable "db_password" {
  description = "Password for the RDS database"
  type        = string
  sensitive   = true
}

# Define the secret key variable
variable "secret_key" {
  description = "Secret key for Django application"
  type        = string
}
