resource "heroku_build" "develop" {
  name     = "${var.heroku_develop_name}"
  region   = "${var.heroku_region}"

  config_vars {
    APP_ENV ="develop"
  }
  buildpacks = "${var.heroku_app_buildpacks}" #["https://github.com/MiguelBarriosAl/Devops-ML"]
}
