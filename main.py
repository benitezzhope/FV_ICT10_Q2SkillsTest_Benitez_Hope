from pyscript import document
# Dictionary containing element information
#element symbol, element name, atomic number, atomic mass
# # KEY : VALUE
nonmetals = {"H": ("H","Hydrogen", 1, 1.008),
             "He": ("He", "Helium", 2, 4.003), 
             "Carbon": ("C", 6, 12.011),
             "Nitrogen":("N", 7, 14.007), }

# Function to search for a element

def search_nm(e):
    # Get the input HTML from HTML    
    Nonmetal = document.getElementById("nonmetal").value
    # Retrieve information from Dictionary
    result = nonmetals.get(Nonmetal, ("Element not found", "-", "-"))
    
    #Display the result in HTML
    #element symbol, element name, atomic number, atomic mass  
    document.getElementById("symbol").innerText = Nonmetal
    document.getElementById("name").innerText = result[1]
    document.getElementById("number").innerText = result[2] 
    document.getElementById("mass").innerText = result[3]
    document.getElementById("result1").style.display = "block"