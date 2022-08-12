
FROM python:3.10-bullseye
# Firefox
RUN apt update && apt install firefox-esr -y
# Add geckodriver
ENV GECKODRIVER_VER v0.31.0
RUN set -x \
   && curl -sSLO https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VER}/geckodriver-${GECKODRIVER_VER}-linux64.tar.gz \
   && tar zxf geckodriver-*.tar.gz \
   && mv geckodriver /usr/bin/
# Python
RUN mkdir -p /root/app
WORKDIR /root/app
COPY . /root/app
RUN pip3 install -r requirements.txt
# JOB
CMD [ "python3", "./Email_Ris_File/main.py"]
# docker build -t jadm333/automatization_lnma_rct .

# docker run -it --rm --env-file ./.env --network=jp -v "$(pwd)/token.json:/root/app/token.json" jadm333/automatization_lnma_rct
# Dev
# docker run --rm -it --entrypoint bash python:3.10-bullseye
# docker run --rm -it --env-file ./.env -v "$(pwd)/token.json:/root/app/token.json" --network=jp --entrypoint bash jadm333/automatization_lnma_rct