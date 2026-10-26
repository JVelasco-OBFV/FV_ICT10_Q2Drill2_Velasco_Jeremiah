from pyscript import display, document

#NO AI WAS USED DURING THE MAKING OF THIS PROJECT
#Random generated names by using this website: https://www.fantasynamegenerators.com/filipino-names.php
def add_brand (e):
    document.getElementById('output1').innerHTML = ""
    grade_seven = {'Glenn Alcantara', 'Arthur Fernandez', 'Meagan Escano'}
    grade_eight = {'Raina Agcaoili', 'Immanuel Arce', 'Jerald Aguilar', 'Kassidy Santos'}
    grade_nine = {'Michelle Acosta', 'Aimee Catubig', 'Inez Estillore'}
    grade_ten = {'Hayden Alonzo', 'Reid Cunanan', 'Tyra Garcia'}
    
    #retrieving values from user's input by ID name
    name_one = document.getElementById('firstname').value
    name_two = document.getElementById('lastname').value

    new_Student = name_one + " " + name_two #concantenates the two inputs with proper spacing
    #assign the value to a set variable
    new_brand_set = {new_Student.title()} #assigning the full name variable as a set datatype, accompanied with proper capitalization

    all_names = grade_seven | grade_eight | grade_nine | grade_ten | new_brand_set #joins all names with the use of the union operator
    total_members = len(grade_seven | grade_eight | grade_nine | grade_ten | new_brand_set) #gets the total length of every item available in each set
    name_list = "<br>".join(sorted(all_names)) #sorts all names alphabetically, including the user's name

    #displays using f string
    document.getElementById('output1').innerHTML = f'<br><h1><b>List of Club Members:</b></h1> <br> {name_list}'
    display(f'Number of Members: {total_members}',target="output1")
