/**
 * Created by marcel on 5/4/15.
 */

function validateForm()
    {
        var departamento = document.forms["registrar_departamento"]["departamento"].value;
        var sigla = document.forms["registrar_departamento"]["sigla"].value;

        if (departamento == null || departamento == "" ||
            sigla == null || sigla == "")
        {
            alert("No se puede registrar un departamento sin todos sus datos.");

            if (departamento == null || departamento == "")
                document.forms["registrar_departamento"]["departamento"].focus();
            else if (sigla == null || sigla == "")
                document.forms["registrar_departamento"]["sigla"].focus();

            return false;
        }
        else
        {
            return true;
        }
    }
