set -e
dir=${PWD}
parentdir="$(dirname "$dir")"

REPO_TAG=$1
FILE=https://raw.githubusercontent.com/mintproject/solution_catalog_api/$REPO_TAG/openapi.yaml
docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v4.1.2 \
     generate  \
     -i $FILE \
     -g python  \
     -o /local/ \
     -c /local/openapi-config.json \
     --git-repo-id solution-catalog-python-api-client \
     --git-user-id mintproject
gsed -i 's~docs/~docs/endpoints/~g' README.md
mkdir -p docs/endpoints
cp README.md docs/endpoints/index.md
mv docs/[A-Z]*.md docs/endpoints/
pushd docs/endpoints/
for file in $(ls *.md); do
    gsed -i 's/README.md//g' $file
done
popd
