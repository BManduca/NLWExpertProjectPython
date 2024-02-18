"""
    Initialized server with Flask
"""

from flask import Flask, request, jsonify
from barcode import Code128
from barcode.writer import ImageWriter

app = Flask(__name__)

@app.route('/create_tag', methods=['POST'])

def create_tag():
    '''
        criando body de uma request, 
        onde essa request vai vir exatamente do Flask e 
        apartir do Flask faremos uma request 
        para a rota 'create_tag'

    '''

    #http protocol
    body = request.json
    product_code = body.get('product_code')


    # extern libraries
    tag_code = Code128(product_code, writer=ImageWriter())
    path_from_tag = f'{tag_code}'
    tag_code.save(path_from_tag)

    #http return
    return jsonify({
        "tag path": path_from_tag
    })

# para rodar servidores em Flask, é preciso definir a função main
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
