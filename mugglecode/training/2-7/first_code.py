import csv

def getweb():
    file = open('/Users/fangjiaqi/github/python-code/mugglecode/web_sample/sample.html', 'r')
    return file.readlines()

def extract_text(html_string):
    lines = []
    for line in html_string:
        new_line = line.strip()
        if new_line.endswith('</td>'):
            formatted = new_line.strip('</td>').split('>')[-1]
            lines.append(formatted)
    return lines

def format_lines(lines):
    unit = []
    formatted_lines = [['Account', 'Due Date', 'Amount', 'Date']]

    for line in lines:
        unit.append(line)
        if len(unit) == 4:
            formatted_lines.append(unit)
            unit = []

    return formatted_lines

def to_csv(formatted_string):
    file = open('result.csv','w+')
    writer = csv.writer(file)
    for unit in formatted_string:
        writer.writerow(unit)

def main():
    html_string = getweb()
    cleaned_text = extract_text(html_string)
    l = format_lines(cleaned_text)
    to_csv(l)

main()
