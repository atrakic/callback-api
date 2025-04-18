yamlfile="$@"
docker run --rm \
    -v $PWD:/local openapitools/openapi-generator-cli generate \
    -i /local/"$yamlfile" \
    -g go \
    -o /local/out/go
