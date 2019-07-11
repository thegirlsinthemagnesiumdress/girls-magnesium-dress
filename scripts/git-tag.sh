# GIT TAG SCRIPT
#!/bin/bash
echo "Latest tag: $(git describe --tags $(git rev-list --tags --max-count=1))"
read -p "Enter new tag: " TAG
echo "Tagging with $TAG";
git tag $TAG
git push --tags
