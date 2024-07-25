import mercadopago
from vars import *

public_key = public_key
token = token

# o link indicará a url que a api deverá devolver a resposta.
def criar_pagamento(itens_pedido, link):
    sdk = mercadopago.SDK(token)

    # itens_pedido são várias instâncias da class ItensPedido, que foi recebida por parâmetro.
    itens = []
    for item in itens_pedido:
        quantidade = int(item.quantidade)
        nome_produto = item.item_estoque.produto.nome
        preco_unitario = float(item.item_estoque.produto.preco)
        itens.append({
            "title" : nome_produto,
            "quantity" : quantidade,
            "unit_price" : preco_unitario
        })

    preference_data = {
        "items": itens,
        "auto_return" : "all",
        # back_urls são links onde os usuários são redirecionados caso o pagamento seja bem-sucedido ou falhe.
        "back_urls": {
            "success" : link,
            "pending" : link,
            "failure" : link
        }
    }

    # aqui nas respostas, há o init_point, que é o link do pagamento.
    resposta = sdk.preference().create(preference_data)
    # print(resposta)
    link_pagamento = resposta["response"]["init_point"]
    print(link_pagamento)

    id_pagamento = resposta["response"]["id"]
    print(id_pagamento)

    # O link (quando printado), mostra o link de checkout. Entre no site do webhook e COLE esse link para ver as informações que são enviadas para ele.  Com o painel do mercado pago, criamos contas de Vendedor e Comprador, basta entrarmos na guia anônima, logarmos no mercadopago developers como COMPRADOR e dps logar no link printado pela função. Após disso, insira os dados dos cartões fakes e veja o resultado.

    return link_pagamento, id_pagamento