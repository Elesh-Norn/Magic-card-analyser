FROM python:3.7-alpine
RUN apk --no-cache add musl-dev linux-headers g++
RUN mkdir -p /pricepuller
WORKDIR /pricepuller
COPY requirements.txt /pricepuller/
RUN pip install -r requirements.txt
COPY . /pricepuller
ENV PYTHONPATH="$PYTHONPATH:/pricepuller"
CMD ["python", "./app/schedule_script.py"]
