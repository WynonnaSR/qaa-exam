FROM python:3.11-alpine

WORKDIR /qaa-exam

COPY requirements.txt ./
COPY tests ./

RUN pip install -r requirements.txt

ENTRYPOINT ["pytest", "-v", "-s", "--alluredir", "allure-results"]
CMD ["test_configuration_calculator.py"]