#!/usr/bin/env python3
from random import randint

lista_npcs = []

player = {
	"nome":"Ko Hur",
	"level":1,
	"exp":0,
	"exp_max":35,
	"hp":100,
	"hp_max":100,
	"dano":25,
}

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

def gerar_npcs(n_npcs):
	for x in range(n_npcs):
		npc = criar_npc(x + 1)
		lista_npcs.append(npc)


def exibir_npcs():
	for npc in lista_npcs:
		exibir_npc(npc)

def exibir_npc():
	print(
		f"Nome: {npc['nome']} // Level: {npc['level']} // dano: {npc['dano']} // HP: {npc['hp']} // exp:{npc['exp']}"
		)

def exibir_player():
	print(
		f"Nome: {player['nome']} // Level: {player['level']} // dano: {player['dano']} // HP: {player['hp']}/{player['hp_max']}  // exp:{player['exp']}/{player['exp_max']}"
		)

def reset_player():
	player['hp'] = player['hp_max']

def reset_npc(npc):
	npc['hp'] = npc['hp_max']

def level_up():
	if player['exp'] >= player['exp_max']:
		player['level'] += 1
		player['exp'] = 0
		player['exp_max'] = player['exp_max'] * 2
		player['hp_max'] += 20
		#reset_player()

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
		print(f"O {npc}['nome'] venceu!")
		exibir_npc(npc)
	level_up()
	reset_player()
	reset_npc(npc)

def atacar_npc(npc):
	npc['hp'] -= player['dano']

def atacar_player(npc):
	player['hp'] -= npc['dano']

def exibir_info_batalha(npc):
	print(f"Player : {player['hp']} // {player['hp_max']}")
	print(f"Npc : {npc['nome']} // {npc['hp']}")
	print("-----------------\n")


gerar_npcs(5)
npc_selecionado = lista_npcs[0]
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
exibir_player()