FROM nardtree/anaconda3-debian-stretch
MAINTAINER nardtree <angeldust03@gmail.com>
EXPOSE 8000
WORKDIR /root/
RUN conda install gunicorn -y
RUN git clone https://github.com/GINK03/minimal-gunicorn-logger-service
WORKDIR /root/minimal-gunicorn-logger-service
CMD sh run_gunicorn.sh
