function gerarOpcao(selector)
{   var i;
    for (i=1;i<=100;i++){
    selector.options[i-1] = new Option(i,i);
    }
    
};