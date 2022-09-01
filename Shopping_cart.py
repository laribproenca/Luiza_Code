cart = []
# Função que adiciona os itens ao carrinho:
def add_item_cart(item):
    cart.append(item)

#Retona todos os itens do carrinho:
def get_all_items_cart():
    return cart.copy()
    
#Retorna item do carrinho com esse id de produto 
def get_item_cart_by_id(id_product):  
    for item in cart:
        if item[1] == id_product:
            return item
       
#Remove o item do carrinho que tem esse produto
def remove_item_id(id_product):
    for item in cart:
        if item[1] == id_product:
            new_cart = cart.remove(item)
            return new_cart

#Programa de Fato:
for i in range(2):
    id_user = input("Insira o id do usuário:")
    id_product = input("Insira o id do produto:")
    price_product = float(input("Insira o preço do produto:"))
    quantity_product = int(input("Insira a quantidade do produto:"))

    item = [id_user, id_product, price_product, quantity_product] 

    add_item_cart(item)

print(" ")
print("O seu carrinho de compra é:", get_all_items_cart())

id = input("Insira o id do produto que deseja remover do carrinho:")
print("O item a ser removido do carrinho é:", get_item_cart_by_id(id))

remove_item_id(id_product)
print("O seu carrinho de compra agora está assim:", get_all_items_cart())


 
 
 