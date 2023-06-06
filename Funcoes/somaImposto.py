def somaImposto(taxaImposto, custo):
    custo_com_imposto = custo + (custo * taxaImposto / 100)
    return custo_com_imposto

taxa = float(input("Digite a taxa de imposto em porcentagem: "))
custo_item = float(input("Digite o custo do item: "))

custo_total = somaImposto(taxa, custo_item)
print("O custo total com imposto é:", custo_total)
