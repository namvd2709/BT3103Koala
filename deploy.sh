#!/usr/bin/env sh

# abort on errors
set -e

# build
npm run build

# navigate into the build output directory
cd dist

git init
git add -A
git commit -m 'deploy'

# if you are deploying to https://<USERNAME>.github.io/<REPO>
# [TODO] : Replace with your username and Repository name
git push -f https://github.com/namvd2709/BT3103Koala.git master:gh-pages

cd -
