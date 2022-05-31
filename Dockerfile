RUN apt update && apt upgrade 
RUN git clone https://github.com/desinobita/AutoAnimeBot
RUN pip3 -m requirements.txt 
CMD python3 bot.py
