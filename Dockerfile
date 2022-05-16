FROM circleci/python

WORKDIR /usr/src/app

COPY pythonPackages.txt ./

RUN sudo apt install portaudio19-dev python3-pyaudio espeak alsa-utils && pip install --no-cache-dir -r pythonPackages.txt

COPY . .

CMD [ "python", "./VoiceAssistant.py" ]

