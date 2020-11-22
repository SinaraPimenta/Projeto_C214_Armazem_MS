function buscarCafe() {
    var input, filtro, ul, li, a, i, txtValue,achouTipo,achouBebida;
    input = document.getElementById('buscar');
    filtro = input.value.toUpperCase();
    tabela = document.getElementById("tabela");
    tr = tabela.getElementsByTagName('tr');
    
    for (i = 1; i < tr.length; i++) {
        achouTipo = false;
        achouBebida = false;
        td = tr[i].getElementsByTagName("td")[0];
        td2 = tr[i].getElementsByTagName("td")[1];
        if(td)
        {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filtro) > -1) 
            {
                tr[i].style.display = "";
                achouTipo = true;
            } 
        }  
        if(td2)
        {
            txtValue = td2.textContent || td2.innerText;
            if (txtValue.toUpperCase().indexOf(filtro) > -1) 
            {
                tr[i].style.display = "";
                achouBebida = true;
            }
        }
        if (achouTipo==false && achouBebida==false) {
            tr[i].style.display = "none";
        }
        
    }
};
function editarCafe(id) {
    location.href = "/cafeicultor/edicaoCafe/?id="+id;
};
function venderCafe(id) {
    location.href = "/cafeicultor/vendaCafe/?id="+id;
};