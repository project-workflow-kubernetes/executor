REMOTE_REPO?=liabifano
DOCKER_NAME=executor
DOCKER_LABEL=latest
GIT_MASTER_HEAD_SHA:=$(shell git rev-parse --short=7 --verify HEAD)

help:
	@echo "build-local"
	@echo "build-and-push"
	@echo "test"



build:
	@docker build -t ${REMOTE_REPO}/${DOCKER_NAME}:${DOCKER_LABEL} .

push:
	@docker tag ${REMOTE_REPO}/${DOCKER_NAME}:${DOCKER_LABEL} ${REMOTE_REPO}/${DOCKER_NAME}:${GIT_MASTER_HEAD_SHA}
	@echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
	@docker push ${REMOTE_REPO}/${DOCKER_NAME}:${GIT_MASTER_HEAD_SHA}


# -@docker run ${REMOTE_REPO}/executor /bin/bash -c "cd executor; py.test --verbose --color=yes"
