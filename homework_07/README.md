
docker run --name postgres_homework07 -p 5432:5432 -e POSTGRES_USER=user -e POSTGRES_PASSWORD=1234 -e POSTGRES_DB=postgres -d postgres

# docker build -t homework_07_image .
# docker run -it --rm homework_07_image