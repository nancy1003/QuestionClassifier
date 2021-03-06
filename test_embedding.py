import wordEmbed
import utils
import configparser
import torch
import numpy as np

global_config_path = './config.ini'

def test_embedding():
  config = configparser.ConfigParser()
  config.read(global_config_path)
  stopword_path = config["GENERAL"]["stop_word_path"]
  datapath = config["GENERAL"]["test_path"]
  pretrain_path = config["WORD_EMBED"]["pretrain_path"]
  x, _ = utils.preprocessing(datapath)
  vo, sents = utils.create_vocab(x, stopword_path)
  vecs = utils.word2vec(vo, sents)
  print(sents[0])
  pretrainVecLayer = wordEmbed.PreTrainEmbedding(vo, pretrain_embedding_path=pretrain_path)
  result = pretrainVecLayer.forward(torch.LongTensor([vecs[0]]))
  print(result)
  # mock bag of word
  pretrainVecLayer_nobow = wordEmbed.PreTrainEmbedding(vo, pretrain_embedding_path=pretrain_path, bow=False)
  temp = pretrainVecLayer_nobow.forward(torch.LongTensor([vecs[0]]))
  temp = torch.sum(temp, 1) / len(vecs[0])
  print(temp)


test_embedding()
