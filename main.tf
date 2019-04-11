provider "aws" {
   region = "us-east-1"
}

resource "aws_instance" "aws_i1" { 
       ami = "ami-0b1d4c689c7949a64" 
       instance_type = "t2.micro" 
tags {
   Name = "aws_vbrr"
  }
#key_name = "lenovo"
key_name = "vreyesr-pc"
#public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAwEQeKrJYomQW5QyqK1oYK1DJMKWacewDtJ7Qq5IUUqfSnxuGs1yLD9s22wm04dCPVKjNnMjpcNbS6Z+B10ZhcBV6HgOwPUIEeP5jLqa8T5wdQwfLUSxT/ZQ9ROGT9FNvGLlzwotR/3x9EXoJfKdDf+pUcQnPkpFKKtzJlFQxVLjXxzwaVQB3cvL1MPHkvrgzDtVMnlxlw0sEI3peW46y14pniJuzjLJFF5DmK66IgD7V2k5ib6CtTvp4IInzTFdyrWwnl95/8ldcAziplrvaG63X7LkwO6j7btLwGKA9AhsbTGoUsD8AXJr61aUfxF2rNKYucrozQ8rshJiywCTm7Q=="

}
