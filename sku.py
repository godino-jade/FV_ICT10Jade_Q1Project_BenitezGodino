from pyscript import display, document

def display_char(e):
    document.getElementById("output1").innerhtml = " "

    categoryname = document.getElementById("category").value
    get_product = document.getElementById("product").value
    get_sq = document.getElementById("stock").value

    SKU = categoryname[:3].upper() + "-" + get_product[:4].upper() + "-" + str(get_sq)

    display(SKU, target="output1") # display the SKU