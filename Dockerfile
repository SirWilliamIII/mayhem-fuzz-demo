FROM ubuntu:22.04

RUN apt update && apt install -y gcc gdb python3

COPY vuln.c /vuln.c
RUN gcc -g -o /vuln /vuln.c

COPY fuzzer.py /fuzzer.py
CMD ["python3", "/fuzzer.py"]

