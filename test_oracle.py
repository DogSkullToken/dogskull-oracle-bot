from bot.oracle import gerar_profecia

print("🔮 Testando gerar profecia...")
try:
    print(gerar_profecia())
except Exception as e:
    print("❌ Erro ao gerar profecia:", e)
