FROM almalinux:8.8

RUN dnf -y update
RUN dnf -y install openssh-server

#ROOTのパスワードを password に変更
RUN echo 'root:password' | chpasswd
RUN dnf -y groupinstall "Development Tools"
RUN dnf -y install \ 
    zip \
    wget \
    openssl \
    openssl-devel \
    openssh-server

RUN ssh-keygen -A
# EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]