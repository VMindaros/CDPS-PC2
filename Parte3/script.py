import os

services = ["product-page", "details", "reviews", "ratings"]

for service in services:
    if service == "reviews":
        os.system("docker run --rm -u root -v '$(pwd)/reviews':/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build")
        os.system("docker build -t g29/reviews:v1 ./reviews/reviews-wlpcfg/")
        os.system("docker build -t g29/reviews:v2 --build-arg \
            enable_ratings=true -t  g29/reviews:v2 ./reviews/reviews-wlpcfg/")
        os.system("docker build --build-arg service_version=v3 --build-arg \
            enable_ratings=true --build-arg star_color=red -t g29/reviews:v3 ./reviews/reviews-wlpcfg/")
    else:
        os.system(f"docker build -f Dockerfile_{service} -t g29/{service} .")

os.system("docker rm -f $(docker ps -aq)")
os.system("docker-compose up")