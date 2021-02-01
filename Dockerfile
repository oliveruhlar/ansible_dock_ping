FROM ubuntu:20.04

RUN apt-get update && apt-get -y upgrade

RUN apt install iproute2 -y

RUN apt-get install -y iputils-ping