
# DB subnet group for RDS instances, using the created subnets
resource "aws_db_subnet_group" "default" {
  name       = "docker-rds-subnet"
  subnet_ids = [aws_subnet.subnet1.id, aws_subnet.subnet2.id]
  tags = {
    Name = "My RDS DB Subnet Group"
  }
}

# Security group for RDS, allows PostgreSQL traffic
resource "aws_security_group" "default" {
  vpc_id      = aws_vpc.default.id
  name        = "DjangoRDSSecurityGroup"
  description = "Allow all inbound traffic for RDS"
  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "allow_all"
  }
}




# RDS instance for Django backend, publicly accessible
resource "aws_db_instance" "default" {
  allocated_storage      = 20
  storage_type           = "gp2"
  engine                 = "postgres"
  engine_version         = "16.1"
  instance_class         = "db.t3.micro"
  identifier             = "my-django-rds"
  db_name                = "djangodb"
  username               = "adam"
  password               = var.db_password
  db_subnet_group_name   = aws_db_subnet_group.default.name
  vpc_security_group_ids = [aws_security_group.default.id]
  skip_final_snapshot    = true
  publicly_accessible    = true
  multi_az               = false

  lifecycle {
    prevent_destroy = true
  }

  tags = {
    Name = "DjangoDockerRDS"
  }
}