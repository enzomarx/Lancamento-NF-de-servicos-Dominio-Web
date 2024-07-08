README - Automação de Lançamento de NF de Serviços no Módulo de Escrituração Fiscal do Dominio Web

Descrição

Este é um projeto de automação que utiliza a biblioteca PyAutoGUI para realizar o lançamento de Notas Fiscais de Serviços no módulo de escrituração fiscal do Dominio Web. O script lê um arquivo CSV que contém informações de NF, como número, data, valor e centavos, e utiliza essas informações para realizar o lançamento das NF no sistema.

Funcionalidades

Lê um arquivo CSV e realiza o lançamento de NF de Serviços no módulo de escrituração fiscal do Dominio Web
Possui uma interface gráfica para selecionar o arquivo CSV e iniciar o script
Possui uma opção para editar o arquivo CSV antes de iniciar o script
Possui uma opção para pausar e retomar o script durante a execução
Exibe o tempo de execução e o número de NF lançadas durante a execução do script
Requisitos

Python 3.x
PyAutoGUI
Pandas
Tkinter
Acesso ao módulo de escrituração fiscal do Dominio Web
Instalação

Instale o Python 3.x em seu computador se você não o tiver instalado ainda.
Instale as bibliotecas necessárias com o comando pip install pyautogui pandas tkinter.
Baixe o código-fonte do projeto e execute o arquivo main.py com o comando python main.py.
Uso

Inicie o script executando o arquivo main.py.
Selecione o arquivo CSV que você deseja utilizar clicando no botão "Selecionar CSV".
Edite o arquivo CSV se necessário clicando no botão "Editar CSV".
Inicie o script clicando no botão "Executar Script".
O script irá realizar o lançamento das NF de Serviços no módulo de escrituração fiscal do Dominio Web com base nas informações contidas no arquivo CSV.
Você pode pausar e retomar o script durante a execução pressionando a tecla "Esc".
Limitações

O script assume que o arquivo CSV está no formato correto e que as informações contidas nele são válidas.
O script não verifica se a NF já foi lançada anteriormente ou se há erros de lançamento.
O script não é responsável por quaisquer erros ou problemas causados por sua execução.
Autor

Enzo Marx Lopes dos Santos

Copyright e Direitos Autorais

Todos os direitos autorais e de propriedade intelectual sobre este projeto pertencem ao autor, Enzo Marx Lopes dos Santos. É proibida a cópia, distribuição, modificação ou uso comercial deste projeto sem a permissão expressa do autor.

Contato

Se você tiver alguma dúvida ou precisar de ajuda, por favor, entre em contato com Enzo Marx Lopes dos Santos em enzomarxsantos@gmail.com