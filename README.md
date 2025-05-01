# Mayhem Fuzz Demo

This is a sample project that demonstrates:

- A vulnerable C binary (buffer overflow)
- A Python fuzzer that triggers crashes
- Docker containerization for isolated testing
- GitHub Actions CI pipeline that auto-fuzzes on every push

## Run Locally

```bash
docker build -t mayhem-fuzz-demo .
docker run --rm mayhem-fuzz-demo
