import typer

app = typer.Typer()

@app.command()
def parse(filename: str):
    with open(filename, "r") as input_file:
        html_text_list = []
        
        for line in input_file:
            html_text_list.append(line)
        
        html_text_full = input_file.read()
    
    # insert javascript into file
    linetextadd1 = "                $a.pause();\n"
    linetextadd2 = "$a.addEventListener('click', () => { if ($a.paused) { $a.play(); } else { $a.pause(); } });\n"
    linetextadd3 = "#timebox { display: block; position: fixed; left: 60%; padding: 10px; margin: 5px; background-color: #666;\n"
    linetextadd4 = "border: 6px solid #000; border-radius: 20px; user-select: text; z-index: 3; pointer-events: auto; line-height: 0.5; }\n"
    linetextadd5 = 	"      <div id=\"timebox\"></div>\n"
    linetextadd6 = "				updateTimebox();\n"
    linetextadd7 = 'function updateTimebox(){ timeBox.innerHTML = \"<span style=\\"color:#fff; font-family: Helvetica, sans-serif; font-size: 16px;\\">(\" + secToTime($a.currentTime) + \")</span>\" }\n'
    linetextadd8 = "function secToTime(t) { return padZero(parseInt((t / (60 * 60)) % 24)) + \":\" + padZero(parseInt((t / (60)) % 60)) + \":\" + padZero(parseInt((t) % 60)); }\n"
    linetextadd9 = "function padZero(v) { return (v < 10) ? \"0\" + v : v; }\n"
    linetextadd10 = "var timeBox = document.getElementById(\"timebox\");\n"
    linetextadd11 = "	updateTimebox();\n"
    
    # specific lines to insert to
    line_insert_to_idx_1 = 205
    line_insert_to_idx_2 = 140
    line_insert_to_idx_3 = 104
    line_insert_to_idx_4 = 105
    line_insert_to_idx_5 = 111
    line_insert_to_idx_6 = 209
    line_insert_to_idx_7 = 308
    line_insert_to_idx_8 = 309
    line_insert_to_idx_9 = 310
    line_insert_to_idx_10 = 144
    line_insert_to_idx_11 = 170
    
    html_text_list[line_insert_to_idx_1 - 1] = linetextadd1
    html_text_list.insert(line_insert_to_idx_2, linetextadd2)
    html_text_list.insert(line_insert_to_idx_3, linetextadd3)
    html_text_list.insert(line_insert_to_idx_4, linetextadd4)
    html_text_list.insert(line_insert_to_idx_5, linetextadd5)
    html_text_list.insert(line_insert_to_idx_6, linetextadd6)
    html_text_list.insert(line_insert_to_idx_7, linetextadd7)
    html_text_list.insert(line_insert_to_idx_8, linetextadd8)
    html_text_list.insert(line_insert_to_idx_9, linetextadd9)
    html_text_list.insert(line_insert_to_idx_10, linetextadd10)
    html_text_list.insert(line_insert_to_idx_11, linetextadd11)
    
    filename_split_at_slash = filename.split("/")
    bare_file_title = filename_split_at_slash[1][:-5]
    
    with open(f"files/{bare_file_title}_parsed.html" , "w") as new_html_file:
        new_html_file.writelines(html_text_list)
    new_html_file.close()
    
if __name__ == "__main__":
    app()