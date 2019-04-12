output "key_name" {
  description = "List of key names of instances"
  value       = ["${aws_instance.aws_i1.key_name}"]
}

output "public_ip" {
   description = "List of Public IP" 
   value       = ["${aws_instance.aws_i1.public_ip}"]
}

output "public_dns" {
   description = "List of the DNS name assigned to the instances"
   value = ["${aws_instance.aws_i1.public_dns}"]
}
