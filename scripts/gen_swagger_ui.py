import argparse

SWAGGER_UI = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="SwaggerUI" />
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
    swagger_ui = SWAGGER_UI
    swagger_ui = swagger_ui.replace("{{ OPEN_API_URL }}", url)
    with open(output_file, "w") as f:
        f.write(swagger_ui)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Swagger UI HTML file")
    parser.add_argument(
        "-u", "--url", type=str, required=True, help="URL for the OpenAPI definition"
    )
    parser.add_argument(
        "-o", "--output", type=str, default="swagger_ui.html",
            help="Output file name (default: swagger_ui.html)",
    )

    args = parser.parse_args()
    generate_swagger_ui(args.url, args.output)
