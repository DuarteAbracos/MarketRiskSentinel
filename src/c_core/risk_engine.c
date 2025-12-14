#include <stdio.h>
#include <stdlib.h> // precisamos disto para malloc e free

//função simples para calcular a média de um array gigante
//recebe um ponteiro para o início do bloco (double* returns) e o tamanho (size)
double calculate_mean(double* returns, int size){
    double sum = 0.0;

    //O segredo da performance está aqui:
    //Estamos a ler memória sequencialmente (i, i+1, i+2, ...)
    for (int i = 0; i < size; i++){
        sum += returns[i];
    }

    return sum / size;
}

/* int main() {
    //Definir o tamanho do monstro
    int  simulations = 1000000; // 1 milhão de cenários

    //Calcular quantos BYTES precisamos
    //Um double gasta 8 bytes. 1 milhão * 8 bytes = ~8 MB
    size_t bytes_needed = simulations * sizeof(double);

    printf("A pedir %.2f MB de RAM ao sistema operativo...\n", bytes_needed / (1024.0 * 1024.0));

    //O MALLOC (Memory Allocation)
    //"Sra. Sistema Operativo, reserve-me este bloco de memória contínuo, por favor."
    double* market_scenarios = (double*)malloc(bytes_needed);

    //Verificação de Segurança (Sempre obrigatório em C profissional)
    if (market_scenarios == NULL) {
        fprintf(stderr, "Erro: Não há memória suficiente!\n");
        return 1;
    }

    printf("Memória alocada com sucesso no endereço%p\n", market_scenarios);

    //Encher o array com dados (Simulação)
    //Como é contíguo, o CPU voa aqui
    for  (int i = 0;  i < simulations; i++) {
        market_scenarios[i] = 0.005; // Vamos fingir que o retorno é 0.5%
    }
    //Processar (chamar a nossa função)
    double mean_val = calculate_mean(market_scenarios, simulations);
    printf("Média calculada pelo Kernel C: %.6f\n", mean_val);

    //O FREE (devolver a chave)
    free(market_scenarios);
    printf("Memória libertada, sem leaks!n");
    return 0;
}
*/