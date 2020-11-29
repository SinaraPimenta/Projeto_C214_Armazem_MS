function gerarOpcao(selector,qtd_atual)
{   var i;
    const fim = parseInt(qtd_atual.placeholder);
    for (i=1;i<=fim;i++){
    selector.options[i-1] = new Option(i,i);
    }
};