import os
from flask import Flask, render_template_string
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route("/")
def maintenance():
    page_title = os.getenv("PAGE_TITLE", "Maintenance")
    headline = os.getenv("HEADLINE", "Site Under Maintenance")
    description = os.getenv("DESCRIPTION", "We are currently performing scheduled maintenance. Please check back soon.")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{page_title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                text-align: center;
                padding: 100px;
            }}
            h1 {{
                color: #333;
            }}
            p {{
                color: #666;
                font-size: 1.2em;
            }}
        </style>
    </head>
    <body>
        <h1>{headline}</h1>
        <p>{description}</p>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=False)
