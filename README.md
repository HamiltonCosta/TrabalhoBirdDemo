Projeto acadêmico desenolvido em Python utilizando a biblioteca Pygame, inspirado na mecânica do clássico Flappy Bird.
O objetivo do jogo é controlar o pássaro, atravessar os obstáculos e alcançar a maior pontuação possível sem colidir com os canos ou com o chão.
O projeto foi desenvolvido como forma de aplicar conceitos de programação, utilização de bibliotecas, controle de versão com Git e modelagem de software.

🎮 Sobre o Jogo

O jogador controla um pássaro utilizando o mouse para fazê-lo voar. Cada clique faz o pássaro subir, enquanto a gravidade faz com que ele desça.

Durante a partida, canos são gerados em posições aleatórias, criando diferentes desafios para o jogador. Ao passar pelos obstáculos, a pontuação é incrementada.

Até o momento o jogo possui:
-Menu inicial (básico);
-Controle do passário com o mouse;
-Animação do personagem;
-Gravidade e movimento vertical;
-Geração aleatória de obstáculos;
-Detecção de colisões;
-Sistema de pontuação;
-Efeitos sonoros;
-Tela de Game Over;
-Botão para reiniciar a partida;

🛠️ Tecnologias e Ferramentas

Python	- Linguagem utilizada no desenvolvimento
Pygame	- Desenvolvimento da interface, sprites, eventos, sons, colisões e controle do jogo
Git	- Controle de versão do projeto
GitHub	- Hospedagem e gerenciamento do repositório
StarUML	- Modelagem e representação do projeto

📚 Conceitos Aplicados

Durante o desenvolvimento do projeto foram aplicados conhecimentos relacionados a:

Programação em Python;
Programação orientada a objetos;
Criação e utilização de classes;
Utilização de bibliotecas externas;
Manipulação de imagens e sons;
Eventos e interação com o usuário;
Sprites e grupos de sprites;
Detecção de colisões;
Geração de valores aleatórios;
Controle de tempo;
Controle de FPS;
Estruturação de um loop principal de jogo;
Controle de versão com Git;
Modelagem de software utilizando StarUML.
🎯 Principais Recursos do Pygame Utilizados
pygame.time.Clock()

Foi utilizado para controlar a velocidade de atualização do jogo.

clock = pygame.time.Clock()
fps = 60

No loop principal:

clock.tick(fps)

Isso limita a execução do jogo a aproximadamente 60 FPS, proporcionando uma atualização mais consistente dos elementos.

Sprites e Groups

O projeto utiliza pygame.sprite.Sprite para representar os objetos do jogo.

Foram criadas classes para:

Bird — representa o personagem;
Pipe — representa os obstáculos;
Button — representa o botão de reinício.

Os objetos Bird e Pipe também são organizados utilizando pygame.sprite.Group, facilitando o gerenciamento e a atualização dos elementos.

Sistema de Colisão

O Pygame também foi utilizado para verificar colisões entre o pássaro e os obstáculos:

pygame.sprite.groupcollide(
    bird_group,
    pipe_group,
    False,
    False
)

Além disso, são verificadas colisões com os limites superior e inferior da tela.

Geração Aleatória

Os obstáculos são criados em posições diferentes utilizando a biblioteca random:

pipe_height = random.randint(-100, 100)

Isso faz com que cada partida possa apresentar diferentes posições para os obstáculos.

⭐ Sistema de Pontuação

A pontuação é incrementada quando o pássaro consegue ultrapassar um conjunto de obstáculos.

A cada ponto conquistado, um efeito sonoro é reproduzido utilizando o sistema de áudio do Pygame.

🔊 Sistema de Áudio

O projeto utiliza arquivos de áudio para aumentar a interação durante a partida.

Foram utilizados sons para:

🪽 Batida de asas;
⭐ Pontuação;
💥 Colisão.

Exemplo:

wing_sound = pygame.mixer.Sound('assets/sons/wing.wav')
point_sound = pygame.mixer.Sound('assets/sons/point.wav')
hit_sound = pygame.mixer.Sound('assets/sons/hit.wav')
📐 Modelagem

A modelagem do projeto foi realizada utilizando o StarUML, permitindo representar a estrutura e o funcionamento do sistema antes e durante o desenvolvimento.

🚀 Como Executar

1. Instalar o Python - https://www.jetbrains.com/pycharm/
2. Baixar/Clonar o repositório
3. Acessar a pasta do projeto pelo pycharm
4. Instalar o Pygame
5. Executar o jogo
6. python main.py
   
========================================================
📖 Objetivo Acadêmico

O desenvolvimento deste projeto teve como objetivo colocar em prática conhecimentos adquiridos durante a formação, principalmente relacionados à linguagem Python, utilização de bibliotecas, programação orientada a objetos, controle de versão e modelagem de software.

Além da implementação do jogo, o projeto proporcionou experiência prática com ferramentas utilizadas no desenvolvimento de software, como Git, GitHub, Pygame e StarUML.

👨‍💻 Autor

Hamilton Costa Gonçalves Junior
