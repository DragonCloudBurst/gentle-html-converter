from bs4 import BeautifulSoup
import typer
import lxml

app = typer.Typer()

@app.command()
def parse(filename: str):
    with open(filename, "r") as input_file:
        html_text = input_file.read()
        
    print(html_text)
    

if __name__ == "__main__":
    app()