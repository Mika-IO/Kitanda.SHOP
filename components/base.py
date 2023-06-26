from alicepy.alice import Component


def base_layout(content):
    kgreen = """
        <style>
        .kgreen {color: #48c794;}
        </style>
    """
    return Component(
        f"""
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">


            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css" />
            <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
            <script src="https://kit.fontawesome.com/your-fontawesome-kit.js"></script>
            <title>Kitanda Shop</title>
            {kgreen}
        </head>
        <body>
            {content}
        </body>
        </html>
        """
    )
