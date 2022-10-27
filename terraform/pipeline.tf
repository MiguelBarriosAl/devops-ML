resource "heroku_build" "devopsml" {
  name     = "${var.heroku_pipeline_name}"
}