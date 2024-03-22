FROM python:3.9

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100


RUN mkdir /app
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN chmod +x startapp.sh

EXPOSE 5000
ENTRYPOINT [ "./startapp.sh" ]
