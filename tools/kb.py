import lxml.etree
import re

## Get XML file using Rapise Spy. Just saving HTML does not work because it is not a valid XML.

url = "https://www.inflectra.com/Support/KnowledgeBase/rapise/List.aspx"
list_file_name = "List.xml"
kb_file_name = "../../docs/Manuals/kb.md"
kb_json_file_name = "Articles.kb"

wspace_regex = re.compile(r"[ \t\n]+", re.IGNORECASE)
kbno_regex = re.compile(r"KB[0-9]+", re.IGNORECASE)

def extract_kbs():
    with open(kb_file_name, "w", encoding='utf-8') as output:
        output.write("# Knowledge Base\n\n")
        output.write("!!! note \"\"\n    We update this list regularly. For the most recent list of KBs please navigate to [Inflectra Knowledge Base](" + url + ")\n\n")
        tree = lxml.etree.parse(list_file_name)    
        headers = tree.xpath("//h5[@class='mb0']/a")
        for h in headers:
            title = h.text.strip()
            href =  "https://www.inflectra.com" + h.attrib["href"]
            m = kbno_regex.search(href)
            kbno = m.group(0)
            p = h.xpath("../..//div[1]")
            if len(p) > 0:
                text =  (''.join(p[0].itertext())).strip()
                text = wspace_regex.sub(" ", text)
            else:
                text = ""
            output.write("### <a onclick=\"return RegisterKbClick('" + kbno + "', '" + title + "')\" target=\"_blank\"  href=\"" + href + "\">" + kbno + "</a> " + title + "\n\n")
            output.write(text + "\n\n")
            
def convert_kbs():
    with open(kb_json_file_name, "w", encoding='utf-8') as output:
        output.write("{ Articles: [")
        tree = lxml.etree.parse(list_file_name)    
        headers = tree.xpath("//h5[@class='mb0']/a")
        delimiter = "\n"
        for h in headers:
            title = h.text.strip()
            title = title.replace("\"", "'")
            href =  "https://www.inflectra.com" + h.attrib["href"]
            m = kbno_regex.search(href)
            kbno = m.group(0)
            p = h.xpath("../..//div[1]")
            if len(p) > 0:
                text =  (''.join(p[0].itertext())).strip()
                text = wspace_regex.sub(" ", text)
                text = text.replace("\"", "'")
                text = text.replace("\\", "\\\\")
                text = text.replace("<", "&lt;")
                text = text.replace(">", "&gt;")
            else:
                text = ""
            output.write(delimiter + '{ Id: "' + kbno + '", Title: "' + title + '", Href: "' + href +  '", Description: "' + text + '"}')
            delimiter = ",\n"
        output.write("\n]}")           

extract_kbs()
convert_kbs()
