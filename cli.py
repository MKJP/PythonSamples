# -*- coding: UTF-8 -*-
"""
Command Line Interface Sample.

"""

import argparse
from pprint import pprint 

class Command(object):
	"""
	"""
	def __init__(self, args):
		# Get argument parse options
		self.args = args

	def create(self):
		id = self.args.id
		amount = self.args.amount
		if id == 0:
			raise Exception("--id is required.")
		if amount == 0:
			raise Exception("--amount is required.")
		txt = 'create(id={}, amount={})'.format(id, amount)
		print(txt)

	def show(self):
		id = self.args.id
		if id == 0:
			raise Exception("--id is required.")
		txt = 'show(id={})'.format(id)
		print(txt)


	def update(self):
		id = self.args.id
		amount = self.args.amount
		if id == 0:
			raise Exception("--id is required.")
		if amount == 0:
			raise Exception("--amount is required.")
		txt = 'update(id={}, amount={})'.format(id, amount)
		print(txt)

	def delete(self):
		id = self.args.id
		if id == 0:
			raise Exception("--id is required.")
		txt = 'delete(id={})'.format(id)
		print(txt)
		
def run(args):
	# クラスメソッドをコール
	try:
		c = Command(args)
		getattr(c, args.command)()
	except Exception as e:
		print(e)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='コマンドラインインターフェースのサンプルコード。')
	# 主要コマンド
	command_list = ['create', 'show', 'update', 'delete']
	command_help = 'create: データを作成する'
	command_help += ' | show: データを確認する'
	command_help += ' | update: データを更新する'
	command_help += ' | delete: データを削除する'
	parser.add_argument('command', type=str, choices=command_list, help=command_help)

	# コマンドオプション指定
	parser.add_argument('--id', type=int, help='ID指定 $ python cli.py show --id 1', default=0)
	parser.add_argument('--amount', type=float, help='数量を指定する $ python cli.py create --id 1 --amount 100.0', default=0)
	
	args = parser.parse_args()
	
	# Get start
	run(args)
	
