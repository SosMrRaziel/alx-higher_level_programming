#!/bin/bash
# a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -o /dev/null -sw "You find me!" 0.0.0.0:5000/catch_me
