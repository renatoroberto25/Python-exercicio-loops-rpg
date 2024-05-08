#!/usr/bin/env python3
from random import randint

# Lista para armazenar NPCs
lista_npcs = []

# Dicionário para armazenar informações do jogador
player = {
	"nome":"",
	"level":1,
	"exp":0,
	"exp_max":35,
	"hp":100,
	"hp_max":100,
	"dano":25,
}

# Função para criar um NPC com base no nível
def criar_npc(level):
	novo_npc = {
		"nome": f"Monstro #{level}",
		"level": level,
		"dano": 5 * level,
		"hp": 100 * level,
		"hp_max": 100 * level,
		"exp":7 * level
	}
	return novo_npc

# Função para gerar NPCs e adicioná-los à lista de NPCs
def gerar_npcs(n_npcs):
	for x in range(n_npcs):
		npc = criar_npc(x + 1)
		lista_npcs.append(npc)

# Função para exibir todos os NPCs na lista de NPCs
def exibir_npcs():
	for npc in lista_npcs:
		exibir_npc(npc)

# Função para exibir informações de um NPC específico
def exibir_npc(npc):
	print(
		f"Nome: {npc['nome']} // Level: {npc['level']} // dano: {npc['dano']} // HP: {npc['hp']} // exp:{npc['exp']}"
		)

# Função para exibir informações do jogador
def exibir_player():
	print(
		f"Nome: {player['nome']} // Level: {player['level']} // dano: {player['dano']} // HP: {player['hp']}/{player['hp_max']}  // exp:{player['exp']}/{player['exp_max']}"
		)

# Função para redefinir a saúde do jogador para o máximo
def reset_player():
	player['hp'] = player['hp_max']

# Função para redefinir a saúde de um NPC para o máximo
def reset_npc(npc):
	npc['hp'] = npc['hp_max']

# Função para aumentar o nível do jogador
def level_up():
	if player['exp'] >= player['exp_max']:
		player['level'] += 1
		player['exp'] = 0
		player['exp_max'] = player['exp_max'] * 2
		player['hp_max'] += 20
		#reset_player()

# Função para iniciar uma batalha entre o jogador e um NPC
def iniciar_batalha(npc):
	while player['hp'] >0 and npc['hp']>0:
		atacar_npc(npc)
		atacar_player(npc)
		exibir_info_batalha(npc)
	if player['hp'] >0:
		print(f"O {player['nome']} venceu! \n {npc['exp']} EXP ganha")
		player['exp'] += npc['exp']
		exibir_player()
	else:
		print(f"O {npc['nome']} venceu!")
		exibir_npc(npc)
	level_up()
	reset_player()
	reset_npc(npc)

# Função para atacar um NPC
def atacar_npc(npc):
	npc['hp'] -= player['dano']

# Função para um NPC atacar o jogador
def atacar_player(npc):
	player['hp'] -= npc['dano']

# Função para exibir informações sobre a batalha
def exibir_info_batalha(npc):
	print(f"Player : {player['hp']} // {player['hp_max']}")
	print(f"Npc : {npc['nome']} // {npc['hp']}")
	print("-----------------\n")

# Gera 5 NPCs para a lista de NPCs
gerar_npcs(5)

# Pedir ao jogador para inserir seu nome
player['nome'] = input("Digite o nome do jogador: ")

# Exibir a lista de NPCs disponíveis
exibir_npcs()

# Pedir ao jogador para selecionar um NPC para batalhar
npc_selecionado_index = int(input("Escolha um número para batalhar com o NPC correspondente: ")) - 1
if npc_selecionado_index >= 0 and npc_selecionado_index < len(lista_npcs):
    npc_selecionado = lista_npcs[npc_selecionado_index]
    iniciar_batalha(npc_selecionado)
else:
    print("Número de NPC selecionado inválido!")

# Exibe as informações do jogador após a batalha
exibir_player()
