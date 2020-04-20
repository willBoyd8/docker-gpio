FROM python:3

# Add the pip dependencies
ADD ./requirements.txt requirements.txt

# Pip install the requirements
RUN pip install -r requirements.txt

# Add the source and move to it's new directory
ADD . /button
WORKDIR /button

# Set the entrypoint
ENTRYPOINT ["python", "/button/main.py"]
