import typer

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
    
    linetextadd1 = "                $a.pause();\n"
    linetextadd2 = "$a.addEventListener('click', () => { if ($a.paused) { $a.play(); } else { $a.pause(); } });\n"
    line_insert_to_idx_1 = 205
    line_insert_to_idx_2 = 140
    
    html_text_list[line_insert_to_idx_1 - 1] = linetextadd1
    html_text_list.insert(line_insert_to_idx_2, linetextadd2)
    
    filename_split_at_slash = filename.split("/")
    bare_file_title = filename_split_at_slash[1][:-5]
    
    with open(f"files/{bare_file_title}_parsed.html" , "w") as new_html_file:
        new_html_file.writelines(html_text_list)
    new_html_file.close()
    
    
if __name__ == "__main__":
    app()