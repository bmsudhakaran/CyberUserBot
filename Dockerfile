# Copyright (C) 2021 FaridDadashzade.
#
# Licensed under MIT license;
# you may not use this file except in compliance with the License.

# All rights reserved.

FROM cyberuserbot/cyber:latest
RUN git clone https://github.com/FaridDadashzade/CyberUserBot /root/CyberUserBot
WORKDIR /root/CyberUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
