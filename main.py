from pyscript import document

def checknam(e):

    cmembers = ["russell adler", "vladimir makarov", "phillip graves", "john mactavish", "frank woods"]

    namef = document.getElementById("fnam").value.lower()
    namel = document.getElementById("lnam").value.lower()
    fullname = namef + " " + namel


    checkingnam = fullname in cmembers


    message = (f'Sorry {fullname}, your name is not on the list.' , f'Congratulations {fullname}! You are now part of the ICT club.')



    document.getElementById("output1").innerHTML = message[checkingnam]








