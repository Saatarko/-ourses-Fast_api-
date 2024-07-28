#!/bin/sh

# Удаление библиотеки, если она установлена
poetry remove fastapi-cache2

# Установка библиотеки вручную
poetry add fastapi-cache2