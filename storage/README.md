# Storage Scripts

Instale a biblioteca ( essa biblioteca não suporta a versão 2.7 do python):

```
pip install --upgrade google-cloud-storage
```

### No Console do Cloud, acesse a página Criar chave da conta de serviço.

1. Acessar página "Criar chave da conta de serviço"
2. Na lista Conta de serviço, selecione Nova conta de serviço.
3. No campo Nome da conta de serviço, insira um nome.
4. Na lista Papel, selecione Projeto > Proprietário.
5. Clique em Criar. O download de um arquivo JSON que contém a chave é feito no computador.

### Após o procedimento acima, precisamos setar a variavel ambiente direcionando para nosso arquivo json de configurações

Com o prompt de comando:

```
set GOOGLE_APPLICATION_CREDENTIALS=[PATH]
```
