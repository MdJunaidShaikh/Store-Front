variable "AWS_ACCESS_KEY" {

    default = "AKIA47CRVOSOFJFJDWUB"
    description = "The acces key for the application"
    type        = string

}

variable "AWS_SECRET_KEY" {

    default = "8eQkzALyE0rYXvb+8sXUZkpjw7NfMVljCaVdWp2W"
}

variable "AWS_REGION" {
  default = "us-east-1"
}

variable "AMIS" {
  type = map(string)
  default = {
    us-east-1 = "ami-0b0ea68c435eb488d"
  }
}

variable "secret_key" {
  description = "The secret key for the application"
  type        = string
}

variable "db_password" {
  description = "The password for the database"
  type        = string
  sensitive   = true
}
