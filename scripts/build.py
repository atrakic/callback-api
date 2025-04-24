import argparse
import yaml, sys
import json

SWAGGER_UI_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>SwaggerUI</title>
    <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5.11.0/swagger-ui.css" />
</head>
<body>
<div id="swagger-ui"></div>
<script src="https://unpkg.com/swagger-ui-dist@5.11.0/swagger-ui-bundle.js" crossorigin></script>
<script>
    window.onload = () => {
        window.ui = SwaggerUIBundle({
            url: '{{ OPEN_API_URL }}',
            dom_id: '#swagger-ui',
        });
    };
</script>
</body>
</html>
"""


def generate_swagger_ui(url, output_file):
    with open(output_file, "w") as file:
        file.write(SWAGGER_UI_TEMPLATE.replace("{{ OPEN_API_URL }}", url))
    print(f"Generated Swagger UI at {output_file}")


def convert_yaml_to_json(yaml_file, output_file):
    with open(yaml_file, "r") as yaml_file_obj:
        with open(output_file, "w") as file:
            json.dump(yaml.safe_load(yaml_file_obj), file, indent=2)
    print(f"Converted {yaml_file} to {output_file}")


def main():
    parser = argparse.ArgumentParser(
        prog=None,
        description="Build helpers for OpenAPI documentation",
        usage="%(prog)s [options] --action <genswaggerui|convert> [--url <url> | --file <file>] [-o <output>]",
        epilog=(
            "Examples:\n"
            "  build.py --action genswaggerui --url http://example.com/openapi.yaml -o index.html \n"
            "  build.py --action convert --file openapi.yaml -o example.json \n"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-a",
        "--action",
        choices=["genswaggerui", "convert"],
        required=True,
        help="Action to perform",
    )
    parser.add_argument("-f", "--file", help="Input YAML file")
    parser.add_argument("-u", "--url", help="URL for the OpenAPI definition")
    parser.add_argument("-o", "--output", help="Output file")
    args = parser.parse_args()

    if args.action == "genswaggerui":
        if not args.url:
            parser.error("--url is required")
        generate_swagger_ui(args.url, args.output or "swagger_ui.html")
    elif args.action == "convert":
        if not args.file:
            parser.error("--file is required")
        convert_yaml_to_json(args.file, args.output or "openapi.json")


if __name__ == "__main__":
    main()
