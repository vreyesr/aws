provider "aws" {
   region = "us-east-1"
}

resource "aws_instance" "aws_i1" { 
       ami = "ami-0b1d4c689c7949a64" 
       instance_type = "t2.micro" 
tags {
   Environmnet = "dev"
  }
key_name = "vreyesr-pc"

}
