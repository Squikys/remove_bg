FROM python:3.13.9-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN python -c "from rembg import new_session; new_session('u2net')"

ENV PORT 8080

EXPOSE 8080

CMD [ "python","main.py" ]