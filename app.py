from create_app import create_app

app = create_app()


@app.context_processor
def inject_app_name():
    return {"app_name": app.name}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
