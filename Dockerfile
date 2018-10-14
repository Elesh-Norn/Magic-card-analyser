FROM python:3
RUN mkdir -p /pricepuller
WORKDIR /pricepuller
COPY requirements.txt /pricepuller/
RUN pip install -r requirement.txt
COPY . /pricepuller
CMD ["python", "./App/schedule_script.py"]