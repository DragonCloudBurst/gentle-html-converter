from bs4 import BeautifulSoup
import typer
import lxml

app = typer.Typer()

@app.command()
def parse(filename: str):
    with open(filename, "r") as input_file:
        line_count = 0
        html_text_list = []
        
        for line in input_file:
            html_text_list.append(line)
            line_count += 1
        
        html_text_full = input_file.read()
    
    linetextadd1 = "    $a.pause();\n"
    line_insert_to_idx = 148
    
    # print(html_text)
    # print(line_count)
    # print(html_text_list[line_insert_to_idx])
    
    html_text_list.insert(line_insert_to_idx, linetextadd1)
    # print(html_text_list[line_insert_to_idx])
    # print(html_text_list[line_insert_to_idx + 1])
    
    filename_split_at_slash = filename.split("/")
    bare_file_title = filename_split_at_slash[1][:-5]
    
    with open(f"{bare_file_title}_parsed.html" , "w") as new_html_file:
        new_html_file.writelines(html_text_list)
    new_html_file.close()
    
    
if __name__ == "__main__":
    app()