## Instalacion Python en Ubuntu

### Habilitamos el repositorio "deadsnakes" que contiene la ultima version de Python

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12
```

## Versiones Instaladas

### Las siguientes dos opciones hacen lo mismo

```bash
ls -l /usr/bin/python*
```

```bash
python3 -V
```

## Indicar la version de python por defecto

```bash
python3 --version
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 2
sudo update-alternatives --config python3  #aqui escogemos la opcion 2
python3 --version
```
