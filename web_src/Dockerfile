
# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:alpine

# If you prefer miniconda:
#FROM continuumio/miniconda3

#explicit group/user
RUN groupadd -r exposedtopublic --gid=1000 && useradd -m -r -g exposedtopublic --uid=1000 exposedtopublic

LABEL Name=hero_restaurant Version=0.0.1
EXPOSE 8000

# Using pipenv:
#RUN python3 -m pip install pipenv
#RUN pipenv install --ignore-pipfile
#CMD ["pipenv", "run", "python3", "-m", "hero_restaurant"]

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m hero_restaurant"

###     ###
# PROJECT #
###     ###

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app /static /media /cache && chown -R exposedtopublic:exposedtopublic /media /cache

WORKDIR /app
ADD .. /app

COPY requirements.txt /requirements.txt
COPY docker-entrypoint.sh /docker-entrypoint.sh
# Using pip:
RUN python3 -m pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["python3", "-m", "hero_restaurant"]

ENV STATIC_ROOT /static
ENV MEDIA_DIR /media
ENV DATA_DIR /cache

COPY . /app

VOLUME ["/static", "/media", "/cache", "/app"]
ENTRYPOINT ["/docker-entrypoint.sh"]