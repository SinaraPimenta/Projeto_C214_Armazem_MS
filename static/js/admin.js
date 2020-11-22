function buscarCafeilcutor() 
{
    var input, filtro, ul, li, a, i, txtValue;
    input = document.getElementById('buscar');
    filtro = input.value.toUpperCase();
    tabela = document.getElementById("tabela");
    tr = tabela.getElementsByTagName('tr');
    for (i = 1; i < tr.length; i++) 
    {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) 
        {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filtro) > -1) 
            {
                tr[i].style.display = "";
            } 
            else {
                tr[i].style.display = "none";
            }
        }
    }
};
function verCafeicultor(id) 
{
    location.href = "/admin/dadosCafeicultor/?id="+id;
};
function editarCafeicultor(id) 
{
    location.href = "/admin/edicaoCafeicultor/?id="+id;
};