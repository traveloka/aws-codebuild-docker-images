## AWS CodeBuild Local Builds


You can now locally test and debug your AWS CodeBuild builds using the new CodeBuild local agent.
Previously, if you wanted to test your AWS CodeBuild build, you had to fully configure and run
CodeBuild. Now, you can simulate a CodeBuild environment locally to quickly troubleshoot the
commands and settings located in the BuildSpec file. The agent also allows you to build your application
locally before committing your changes to build on the cloud.

Start by pulling the signed local agent image from [DockerHub](https://hub.docker.com/r/amazon/aws-codebuild-local/):

    docker pull amazon/aws-codebuild-local:latest --disable-content-trust=false


You can verify the SHA matches our [latest release](https://docs.aws.amazon.com/codebuild/latest/userguide/samples.html). Please allow at least an hour after a new version has been pushed for the updated SHA to be reflected in our documentation. 

Download and use our codebuild_build.sh script to run your local builds.

usage: codebuild_build.sh [-i image_name] [-a artifact_output_directory] [options]

**Required:**  
  -i        Used to specify the customer build container image.  
  -a        Used to specify an artifact output directory.  

**Optional:**  
  -s        Used to specify a source directory. Defaults to the current working directory.  
  -c        Use the AWS configuration and credentials from your local host. This includes ~/.aws and any AWS_* environment variables.  
  -b        Used to specify a buildspec override file. Defaults to buildspec.yml in the source directory.  
  -e        Used to specify a file containing environment variables.  

**Environment variable file format:**
  * Expects each line to be in VAR=VAL format
  * Lines beginning with # are processed as comments and ignored
  * Blank lines are ignored
  * File can be of type .env or .txt
  * There is no special handling of quotation marks, meaning they will be part of the VAL

Note that if you want to use an AWS CodeBuild Curated image, you can build it locally on your machine by cloning this repository and performing a docker build on your choice of image.
