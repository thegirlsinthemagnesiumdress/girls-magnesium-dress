#!/bin/bash

usage(){
    echo "Usage:";
    echo "    $(basename "$0") [-h] {major|minor|patch} -- Deploy a release";
    echo "    where:";
    echo "         h--help  show this help text";
    echo "         major  increment major release number";
    echo "         minor  increment minor release number";
    echo "         patch  increment patch release number";
}

# fetch tags from remote
git fetch --tags;

VERSION_INCREASE="$1";
VERSION=$(git describe --abbrev=0 --tags 2>/dev/null)


if [ -z $VERSION ];
then
    echo "Never been tagged before....";
    NEW_TAG=0-0-1;
else
    VERSION_BITS=(${VERSION//-/ })

    if [[ ${#VERSION_BITS[@]} < 3 ]];
    then
        echo "Tag not in proper format. Expected tag format x-y";
        exit 1;
    fi

    VNUM1=${VERSION_BITS[0]}
    VNUM2=${VERSION_BITS[1]}
    VNUM3=${VERSION_BITS[2]}

    case "$VERSION_INCREASE" in
            major)
                VNUM1=$((VNUM1+1))
                VNUM2=$((0))
                VNUM3=$((0))
                ;;
            minor)
                VNUM2=$((VNUM2+1))
                VNUM3=$((0))
                ;;
            patch)
                VNUM3=$((VNUM3+1))
                ;;
            *)
                usage;
                exit 1;

    esac

    NEW_TAG="$VNUM1-$VNUM2-$VNUM3";

    echo "Updating $VERSION to $NEW_TAG";
fi

#get current hash and see if it already has a tag

NEEDS_TAG=$(git describe --tags --contains HEAD 2>/dev/null)

if [ -z "$NEEDS_TAG" ]; then
    echo "Tagged with $NEW_TAG";
    git tag $NEW_TAG;
    git push origin $NEW_TAG;
else
    echo "Already a tag on this commit";
    exit 1;
fi

