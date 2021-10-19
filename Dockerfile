FROM mcr.microsoft.com/playwright
CMD [ "python", "run.py" ]
WORKDIR /app
VOLUME /app
RUN chown pwuser:pwuser . && pip install playwright==1.15.3
COPY --chown=pwuser:pwuser . /app/

