from flask import Flask,request
import base64
from lxml import etree
app = Flask(__name__)

@app.route('/')
def index():
    return open(__file__).read()


@app.route('/parse',methods=['POST'])
def parse():
    xml=request.form.get('xml')
    print(xml)
    if xml is None:
        return "None"
    parser = etree.XMLParser(load_dtd=True, resolve_entities=True)
    root = etree.fromstring(xml, parser)
    name=root.find('name').text
    return name or None



if __name__=="__main__":
    app.run(host='0.0.0.0',port=8000)