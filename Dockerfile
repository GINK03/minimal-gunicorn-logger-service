FROM nardtree/anaconda3-debian-stretch
MAINTAINER nardtree <angeldust03@gmail.com>
EXPOSE 8000
WORKDIR /root/
RUN conda install gunicorn -y
RUN git clone https://github.com/GINK03/loose-coupling-json-over-http
WORKDIR /root/loose-coupling-json-over-http/python-gunicorn-flask
CMD sh run_gunicorn.sh
