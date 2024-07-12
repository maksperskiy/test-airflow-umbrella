FROM alpine

RUN apk update && \
    apk add --update git && \
    apk add --update openssh

RUN mkdir -p /root/.ssh

ARG UMBRELLA_REPOSITORY_SSH_KEY
RUN echo "${UMBRELLA_REPOSITORY_SSH_KEY}" > /root/.ssh/id_rsa
RUN chmod -R 600 /root/.ssh/

ARG GIT_REMOTE
RUN ssh-keyscan -t rsa $GIT_REMOTE >> /root/.ssh/known_hosts

RUN echo "IdentityFile /root/.ssh/id_rsa" >> /etc/ssh/ssh_config
RUN echo -e "StrictHostKeyChecking no" >> /etc/ssh/ssh_config


ARG UMBRELLA_REPOSITORY
RUN git clone $UMBRELLA_REPOSITORY /opt/umbrella

WORKDIR /opt/umbrella

RUN chmod +x ./sync.sh

ENTRYPOINT ["./sync.sh"]
