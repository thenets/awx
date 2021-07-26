FROM centos:8

RUN set -x \
    # Install OS dependencies
    && dnf install -y git podman curl python3-pip \
    # Install Ansible
    && pip3 install --upgrade pip setuptools-rust wheel \
    && pip3 install ansible-runner

RUN set -x \
    # Install receptor
    && curl -Ls --output /usr/local/bin/receptor https://www.dropbox.com/s/wv2bx00lxmzqjlr/receptor?dl=1 \
    && chmod +x /usr/local/bin/receptor

RUN set -x \
    # Install receptorctl
    && pip install git+git://github.com/ansible/receptor.git#subdirectory=receptorctl
