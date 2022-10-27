provider "heroku" {
  version = "~> 7.65.0"
  email = "${var.heroku_account_email}"
  api_key = "${var.heroku_api_key}"
}

output "output_git_url" {
  value = "${heroku_build.develop}"
}