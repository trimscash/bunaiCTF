FROM ubuntu:22.10

RUN apt-get update && apt-get upgrade
RUN apt-get -y install xinetd
RUN groupadd -r user && useradd -r -g user user


COPY --chown=root:user ./build/start.sh /home/user/start.sh
COPY --chown=root:user ./build/flag /home/user/flag
COPY --chown=root:user ./src/vuln /home/user/vuln
COPY --chown=root:root ./build/pwn.xinetd /etc/xinetd.d/pwn


WORKDIR /home/user

RUN chmod 444 ./flag
RUN chmod 555 ./vuln
RUN chmod 444 ./start.sh
RUN chmod 444 /etc/xinetd.d/pwn

USER user
EXPOSE 30001

CMD ["xinetd","-dontfork","-f","/etc/xinetd.d/pwn"]
#CMD ["systemctl", "start", "xinetd"]
