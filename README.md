# nQueens

## Pre-requisits
+ Docker
+ Docker-compose

## Build and run the application containers

Build containers (only the first time):

```bash
cd cuenca-test
docker-compose up -d --build

```

After this, whenever you want to run the application just execute from the root directory.
```bash
docker-compose up -d

```

## Running App
Type the following command

```bash
docker-compose exec app bash
python queens.py

```

## Running Tests
```bash
docker-compose exec app bash
pytest tests.py

```
