#!/bin/bash
if pgrep -x "mpv" >/dev/null
then
	echo 'Programa já em execução !!!'
else
	echo 'Carregando...'
	echo 'Aguarde alguns segundos(10-30s) com o *Terminal ABERTO* !!!'
	mpv --no-video --shuffle "https://www.youtube.com/playlist?list=PLwBgF1GY-BCd0mdNoogW8zvtw-ga5yzSM"
fi
