#!/usr/bin/env bash

TARGET_REPO=${TRAVIS_REPO_SLUG}

echo $TARGET_REPO

git push -fq https://${GH_TOKEN}@github.com/$TARGET_REPO.git master > /dev/null
