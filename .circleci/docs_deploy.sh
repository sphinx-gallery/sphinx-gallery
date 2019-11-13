#!/bin/sh
# ideas used from https://gist.github.com/motemen/8595451

# abort the script if there is a non-zero error
set -e

# show where we are on the machine
pwd
ls ${PWD}

siteSource="$1"
destDir="$2"

if [ ! -d "$siteSource" ] || [ -z "$destDir" ];
then
    echo "Usage: $0 <site source dir> <site dest dir>, got: "
    echo "    $@"
    exit 1
fi

# now lets setup the docs repo so we can update them with the current build
git config --global user.email "Circle CI" > /dev/null 2>&1
git config --global user.name "bot@try.out" > /dev/null 2>&1
git clone git@github.com:sphinx-gallery/sphinx-gallery.github.io.git

siteSource="${PWD}/${siteSource}"
cd sphinx-gallery.github.io/
mkdir -p ${destDir}
destDir="${PWD}/${destDir}"
echo "Copying ${siteSource} to ${destDir}"

# copy over or recompile the new site
git rm -rf ${destDir}
cp -a ${siteSource} ${destDir}
cp dev/binder/requirements.txt binder/requirements.txt

# stage any changes and new files
git add -A
# now commit
git commit --allow-empty -m "Update the docs: ${CIRCLE_BUILD_URL}"
# and push, but send any output to /dev/null to hide anything sensitive
git push --force --quiet origin master > /dev/null 2>&1

# go back to where we started
cd ..

echo "Finished Deployment!"
