import os
from dotenv import load_dotenv
from translation_flaskapp import create_app

def main():

    # Load environment variables from .env file
    load_dotenv()

    # Read environment variables for configuration
    host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_RUN_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 'yes')

    app = create_app()
    app.run(host=host, port=port, debug=debug)

if __name__ == "__main__":
    main()
