#!/bin/bash
appid=gweb-digitalmaturity-staging

# fetch tags from remote
git fetch --tags;

DEFAULT_TAG="0-0-1"
HASH=$(git rev-parse --short=5 --dirty HEAD)
LATEST_TAG=$(git describe --abbrev=0 --tags 2>/dev/null)
DEPLOYMENT_TYPE="$1";


usage(){
    echo "Usage:";
    echo "    $(basename "$0") [-h] {major|minor|patch} -- Deploy a release";
    echo "    where:";
    echo "         h--help  show this help text";
    echo "         major  increment major release number";
    echo "         minor  increment minor release number";
    echo "         patch  increment patch release number";
}


if [ -z $LATEST_TAG ];
then
    LATEST_TAG="$DEFAULT_TAG-$HASH";
else
    LATEST_TAG=$LATEST_TAG-$HASH;
fi


case "$DEPLOYMENT_TYPE" in
        major)
            DEPLOYMENT_TYPE=major;
            ;;
        minor)
            DEPLOYMENT_TYPE=minor;
            ;;
        patch)
            DEPLOYMENT_TYPE=patch;
            ;;
        "")
            DEPLOYMENT_TYPE="";
            ;;
        *)
            usage;
            exit 1;
esac

VERSION_ADDED=0;

if [ ! -z $DEPLOYMENT_TYPE ]; then
    echo "Tagging commit..";
    ./scripts/versions.sh $DEPLOYMENT_TYPE &>/dev/null;
    VERSION_ADDED=$?;
    LATEST_TAG=$(git describe --abbrev=0 --tags 2>/dev/null)
fi


echo "Deploying with tag: $LATEST_TAG";

if [ ! "$VERSION_ADDED" = 0 ]; then
    echo "Something went wrong tagging the version";
    exit;
fi

./manage.py gulp build --settings=core.settings.live
python manage.py collectstatic --settings=core.settings.live
./third_party/google_appengine/appcfg.py update --no_cookies -A $appid -V $LATEST_TAG ./src
