from pyscript import document, display

def display_char(e):
    document.getElementById("output2").innerHTML = " "  # clears previous result

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
    tax_rate = 0.12  
    tax = subtotal * tax_rate
    
    # Grand total
    total = subtotal + size_price + tax + 

    display(f"Total: P{total}.", target="output1")
    display(f"Subtotal: P{subtotal}.", target="output1")
    display(f"Tax: P{tax}.", target="output1", append=True)
    display(f"Thank you for your order!", target="output1", append=True)
