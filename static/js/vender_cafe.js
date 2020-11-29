function gerarOpcao()
{
    inicio = 1
    fim = parseInt(document.getElementById("valor-total-bar").placeholder);
    document.getElementById("qtd").innerHTML="";   
    selector = document.getElementById("qtd");
    var i;
    for (i=inicio;i<=fim;i++){
        selector.options[i] = new Option(i,i);
    }
};

