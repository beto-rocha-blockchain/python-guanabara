# Solicita ao usuário a largura e a altura da parede
largura = float(input("Digite a largura da parede (m): "))
altura = float(input("Digite a altura da parede (m): "))
 
# Calcula a área da parede
area = largura * altura
 
# Considerando que cada litro de tinta cobre 2m²
litros_tinta = area / 2
 
# Exibe os resultados
print(f"\nA área da parede é de {area:.2f} m².")
print(f"Você precisará de aproximadamente {litros_tinta:.2f} litros de tinta para pintá-la.")