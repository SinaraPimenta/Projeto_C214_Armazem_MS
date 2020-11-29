function gerarOpcao(selector)
{   var i;
    for (i=0;i<=100;i++){
    selector.options[i] = new Option(i,i);
    }
};