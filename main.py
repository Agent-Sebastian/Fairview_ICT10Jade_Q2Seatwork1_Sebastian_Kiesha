from pyscript import document

def checknam(e):

    cmembers = ["russell" + "adler", "vladimir" + "makarov", "phillip" + "graves", "john" + "mactavish", "frank" + "woods"]

    namef = document.getElementById("fnam").lower
    namel = document.getElementById("lnam").lower



    checkingnam =  namef + namel in cmembers


    message = (f'Member "{namef} {namel}" not found.' , f'Member found. Welcome, {namef} {namel}.')



    document.getElementById("output1").innerHTML = message[checkingnam]








"""
 namef = document.getElementById("fnam").lower
namel = document.getElementById("lnam").lower




cmembersf = ["Russell", "Vladimir", "Phillip", "John", "Frank"]
cmembersl = ["Adler", "Makarov", "Graves", "Mactavish", "Woods"]

cmembers = ["Russell" + "Adler", "Vladimir" + "Makarov", "Phillip" + "Graves", "John" + "Mactavish", "Frank" + "Woods"]

cmembers = ["Russell Adler", "Vladimir Makarov", "Phillip Graves", "John Mactavish", "Frank Woods"]


"""