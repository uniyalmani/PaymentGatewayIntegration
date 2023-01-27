FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install  -r requirements.txt

COPY . .

ENV SECRET_KEY="qwertyuiopasdfghjklzxcvbnmgenratedfjsdfjs"
ENV ALGORITHM="HS256"
ENV ACCESS_TOKEN_EXPIRE_MINUTES=50
ENV NAME="nitin"
ENV EMAIL="nitinuniyal21@gmail.com"
ENV PASSWORD=9410197255
ENV DB_URL="postgresql://encwsezklfjgzf:af5a4ed0df503805cd1cd5aacae46ccd2881ced1d01588916205e71881287ff9@ec2-35-168-194-15.compute-1.amazonaws.com:5432/d9gmak7qi2ssqh"

CMD [ "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port",  "8000"]
# CMD uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000} 
# web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000}
# CMD web: gunicorn --bind 0.0.0.0:$PORT app.main:app
# CMD web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000} 