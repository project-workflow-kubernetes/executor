[![Build Status](http://img.shields.io/travis/liabifano/ml-aws.svg?style=flat)](https://travis-ci.com/project-workflow-kubernetes/executor)


# executor

Repository that contains the necessary information to build the image base for the jobs.


### To build image locally
```bash
make build
```


### To push the image
You must have `DOCKER_USERNAME` and `DOCKER_PASSWORD` available in the environment.
```bash
make push
```
