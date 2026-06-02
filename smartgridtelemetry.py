import random
import time

class TelemetriaMedidores:
    def __init__(self, volume_leituras):
        self.volume_leituras = volume_leituras

    def processar_fluxo_consumo(self):
        registro_atual = 1
        while registro_atual <= self.volume_leituras:
            consumo_ativo = round(random.uniform(0.5, 25.0), 2)
            yield {
                "id_medidor": f"MED-{random.randint(10000, 99999)}",
                "registro_n": registro_atual,
                "consumo_kwh": consumo_ativo,
                "status_rede": "Operação Normal" if consumo_ativo < 20.0 else "Demanda de Pico Flutuante"
            }
            registro_atual += 1

if __name__ == "__main__":
    pipeline_telemetria = TelemetriaMedidores(volume_leituras=5)
    fluxo_dados = pipeline_telemetria.processar_fluxo_consumo()

    print("=== [SMC] INICIANDO RECONHECIMENTO DE TELEMETRIA EM TEMPO REAL ===\n")

    for registro in fluxo_dados:
        print(f"Medidor: {registro['id_medidor']} | Reg. #{registro['registro_n']} | "
              f"Consumo Ativo: {registro['consumo_kwh']} kWh | Condição: {registro['status_rede']}")
        time.sleep(1)

    print("\n=== [SMC] FLUXO DE DADOS CONCLUÍDO COM SUCESSO ===")