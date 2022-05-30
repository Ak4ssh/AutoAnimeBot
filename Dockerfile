RUN apt update && apt upgrade 

RUN pip3 install -U -r requirements.txt 

CMD ["python3","-m","bot.py"]
