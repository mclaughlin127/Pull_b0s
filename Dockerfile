# Dockerfile, Image, Container

FROM python:3.9

ADD pull_b0s.py .

RUN pip install nibabel numpy dipy argparse

ENTRYPOINT [ "python", "pull_b0s.py" ]