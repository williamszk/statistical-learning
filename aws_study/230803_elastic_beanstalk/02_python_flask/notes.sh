# https://www.sitepoint.com/aws-elastic-beanstalk-beginner-tutorial/

mkdir my-elastic-beanstalk-app
cd my-elastic-beanstalk-app


# zip -r my-elastic-beanstalk-app.zip my-elastic-beanstalk-app # the problem with this is that it will include the parent dir too
rm my-elastic-beanstalk-app.zip
(cd my-elastic-beanstalk-app && zip -r ../my-elastic-beanstalk-app.zip .)
