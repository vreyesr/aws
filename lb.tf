resource "aws_elb" "lb-vr2" {
  # (resource arguments)
  name = "lb-vr2"
  listener = [{
      instance_port = 3000
      instance_protocol = "http"
      lb_port = 3333
      lb_protocol = "http"
      ssl_certificate_id = ""
      },{
      instance_port = 22
      instance_protocol = "tcp"
      lb_port = 2222
      lb_protocol = "tcp"
      ssl_certificate_id = ""
      }]
  connection_draining = true
  idle_timeout = 300
}
