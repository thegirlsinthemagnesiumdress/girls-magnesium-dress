# #!/bin/bash
# appid_staging=gweb-digitalmaturity-staging

# appid_prod=gweb-digitalmaturity

# # fetch tags from remote
# git fetch --tags;

# DEFAULT_TAG="0-0-1"
# HASH=$(git rev-parse --short=5 --dirty HEAD)
# LATEST_TAG=$(git describe --abbrev=0 --tags 2>/dev/null)
# DEPLOYMENT_TYPE="$1";
# PROD_FLAG=''

# while getopts 'p' flag; do
#   case "${flag}" in
#     p) PROD_FLAG='true' ;;
#     *) echo 'Use -p flag to deploy to production'
#        exit 1 ;;
#   esac
# done


# if [ $PROD_FLAG ];
# then
#     appid=$appid_prod
# else
#     appid=$appid_staging
# fi


# usage(){
#     echo "Usage:";
#     echo "    $(basename "$0") [-h] {major|minor|patch} -- Deploy a release";
#     echo "    where:";
#     echo "         h--help  show this help text";
#     echo "         major  increment major release number";
#     echo "         minor  increment minor release number";
#     echo "         patch  increment patch release number";
# }


# if [ -z $LATEST_TAG ];
# then
#     LATEST_TAG="$DEFAULT_TAG-$HASH";
# else
#     LATEST_TAG=$LATEST_TAG-$HASH;
# fi


# case "$DEPLOYMENT_TYPE" in
#         major)
#             DEPLOYMENT_TYPE=major;
#             ;;
#         minor)
#             DEPLOYMENT_TYPE=minor;
#             ;;
#         patch)
#             DEPLOYMENT_TYPE=patch;
#             ;;
#         "")
#             DEPLOYMENT_TYPE="";
#             ;;
#         *)
#             usage;
#             exit 1;
# esac

# VERSION_ADDED=0;

# if [ ! -z $DEPLOYMENT_TYPE ]; then
#     echo "Tagging commit..";
#     ./scripts/versions.sh $DEPLOYMENT_TYPE &>/dev/null;
#     VERSION_ADDED=$?;
#     LATEST_TAG=$(git describe --abbrev=0 --tags 2>/dev/null)
# fi


# echo "Deploying with tag: $LATEST_TAG";

# if [ ! "$VERSION_ADDED" = 0 ]; then
#     echo "Something went wrong tagging the version";
#     exit;
# fi

# ./manage.py gulp build --settings=core.settings.live
# python manage.py collectstatic --settings=core.settings.live
# ./third_party/google_appengine/appcfg.py update --no_cookies -A $appid -V $LATEST_TAG ./src


# TEMPORARY QUICK FIX
#!/bin/bash
read -p "Enter version: " VERSION
echo "Deploying with tag: $VERSION";

./manage.py gulp build --settings=core.settings.live
python manage.py collectstatic --settings=core.settings.live
./third_party/google_appengine/appcfg.py update --no_cookies -A gweb-digitalmaturity-staging -V $VERSION ./src
