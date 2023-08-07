# https://www.sitepoint.com/aws-elastic-beanstalk-beginner-tutorial/

mkdir my-elastic-beanstalk-app
cd my-elastic-beanstalk-app


# zip -r my-elastic-beanstalk-app.zip my-elastic-beanstalk-app # the problem with this is that it will include the parent dir too
cd -
rm my-elastic-beanstalk-app.zip
(cd my-elastic-beanstalk-app && zip -r ../my-elastic-beanstalk-app.zip .)

cd my-elastic-beanstalk-app
# docker build -t username/beanstalk-flask .
# docker compose up
touch Dockerrun.aws.json

docker build -t williamszk/beanstalk-flask:latest .
docker tag williamszk/beanstalk-flask:latest williamszk/getting-started:latest
docker push williamszk/getting-started:latest


# to login the first time:
docker login

docker compose up
cd -


rm my-elastic-beanstalk-app-2.zip
(cd my-elastic-beanstalk-app-2 && zip -r ../my-elastic-beanstalk-app-2.zip .)
