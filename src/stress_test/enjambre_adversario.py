import asyncio
import random
import aiohttp

# =====================================================================
# VITALIS-PRIME: ADVERSARIAL SWARM
# ARCHITECT: JORGE HUMBERTO DAVALOS GONZALEZ
# =====================================================================

async def run_swarm():
    URL = "http://127.0.0.1:5000/api/v1/telemetria/feedback"
    print("☢️ Iniciando Enjambre Adversario...")

    async def send(session, ronda):
        t, e, a = round(random.uniform(0.5, 10.0), 2), round(random.uniform(0.1, 5.0), 3), round(random.uniform(0.1, 1.0), 4)
        if 7 <= ronda <= 13:
            res = "fallo_critico" if (t < 4.0 and e < 2.0) else "colapso_estable"
        else:
            res = "fallo_critico" if (t > 7.0 or e > 3.5) else "colapso_estable"

        payload = {"metricas_internas": {"temperatura_q": t, "entropia_shannon": e, "amplitud_base": a}, "resultado_real": res}
        try:
            async with session.post(URL, json=payload) as r: return r.status == 202
        except: return False

    async with aiohttp.ClientSession() as session:
        for r in range(1, 21):
            print(f"--- Ronda {r}/20 ---")
            tasks = [send(session, r) for _ in range(150)]
            await asyncio.gather(*tasks)
            await asyncio.sleep(1.5)
    print("🏁 Protocolo finalizado.")

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(run_swarm())
