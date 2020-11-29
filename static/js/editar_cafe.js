function gerarOpcao()
{
    inicio = 0
    fim = 100
    selector = document.getElementById("qtd");
    var i;
    for (i=inicio;i<=fim;i++){
    selector.options[i] = new Option(i,i);
    }
};