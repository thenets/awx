FROM centos:8

RUN set -x \
    # Install OS dependencies
    && dnf install -y podman curl python3-pip \
    # Install Ansible
    && pip3 install --upgrade pip setuptools-rust wheel \
    && pip3 install ansible-runner

RUN set -x \
    # Install Receptor
    && curl -Ls --output /usr/local/bin/receptor https://www.dropbox.com/s/wv2bx00lxmzqjlr/receptor?dl=1 \
    && chmod +x /usr/local/bin/receptor
