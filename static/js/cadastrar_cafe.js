function gerarOpcao()
{
    inicio = 1
    fim = 100
    selector = document.getElementById("formControlQtd");
    var i;
    for (i=inicio;i<=fim;i++){
    selector.options[i-1] = new Option(i,i);
    }
};