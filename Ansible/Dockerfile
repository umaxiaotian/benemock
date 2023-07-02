FROM almalinux:8.8
RUN dnf -y update
RUN dnf -y install openssh-server
#ROOTのパスワードを password に変更
RUN echo 'root:password' | chpasswd
RUN dnf -y groupinstall "Development Tools"
RUN dnf -y install \ 
    kernel-devel \
    kernel-headers \
    gcc-c++ \
    patch \
    libffi-devel \
    autoconf \
    automake \
    make \
    libtool \
    bison \
    tk-devel \
    zip \
    wget \
    tar \
    gcc \
    zip \
    wget \
    openssl \
    openssl-devel \
    openssh-server \
    sshpass
RUN wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz
RUN tar -xzf Python-3.11.0.tgz
RUN cd Python-3.11.0
RUN Python-3.11.0/configure
RUN make
RUN make install

RUN dnf -y install python3-pip epel-release
RUN pip3 install --upgrade setuptools
RUN pip3 install -U pip
# RUN pip3 --version
RUN pip3 install ansible
RUN pip3 install fastapi uvicorn
COPY ./app /app 
WORKDIR /app

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]