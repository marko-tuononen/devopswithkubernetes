FROM python:3.7

LABEL maintainer="marko.tuononen@gmail.com"

RUN useradd --create-home appuser
USER appuser

ADD log_output.py /home/appuser/

WORKDIR /home/appuser

CMD ["python3", "log_output.py"]
