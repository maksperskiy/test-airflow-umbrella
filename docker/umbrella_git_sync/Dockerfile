ARG UMBRELLA_REPOSITORY="ssh://git@gitlab.intexsoft.by:222/<umbrella_repository>.git"

FROM alpine/git:latest

RUN $UMBRELLA_REPOSITORY_SSH_KEY > /root/.ssh/id_ed25519

WORKDIR /opt/
RUN git clone ${UMBRELLA_REPOSITORY} umbrella
WORKDIR /opt/umbrella

RUN chmod +x /your-script.sh

ENTRYPOINT ["./sync.sh"]
