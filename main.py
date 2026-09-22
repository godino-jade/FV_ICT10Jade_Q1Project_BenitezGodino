from pyscript import document, display

def create_order(e):
    document.getElementById("output1").innerHTML = " "  # clears previous result

    # Get each item element
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")

    # Calculate subtotal 
    subtotal = (float(prod1.value) * prod1.checked
                + float(prod2.value) * prod2.checked
                + float(prod3.value) * prod3.checked
                + float(prod4.value) * prod4.checked
                + float(prod5.value) * prod5.checked)       

    # Tax and price with tax
    tax_rate = 0.12 # VAT OF 12%
    tax = subtotal * tax_rate # order total + tax
    
    # Grand total
    total = subtotal + tax 

    display(f"Total: ₱{total}.", target="output1", append=True)
    display(f"Subtotal: ₱{subtotal}.", target="output1", append=True)
    display(f"Tax: ₱{tax}.", target="output1", append=True)
    display(f"Thank you for your order!", target="output2", append=True)