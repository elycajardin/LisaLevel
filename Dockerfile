FROM python:latest
RUN mkdir LisaLevel
RUN mkdir LisaLevel/dict.csv
COPY main.py ./LisaLevel
COPY requirements.txt ./LisaLevel
RUN pip install --upgrade pip
RUN pip install -r ./LisaLevel/requirements.txt
CMD ["python", "LisaLevel/main.py"]